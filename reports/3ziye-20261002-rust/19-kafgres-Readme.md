# kafgres

A PostgreSQL extension that embeds a Kafka broker. Unmodified Kafka clients (librdkafka,
the Java client, Sarama, kafka-python, `kcat`, the `kafka-*.sh` tooling) connect to
Postgres on port 9092 and cannot tell the difference. Topics, partitions, offsets,
consumer groups, and the log itself live in the database.

The goal is transactional coupling between the database and the event stream:

```sql
BEGIN;
  INSERT INTO orders (id, customer_id, total) VALUES (...);
  SELECT kafgres_produce('order-events', 'OrderCreated',
                         jsonb_build_object(...)::text);
COMMIT;
```

Both commit or neither does. There is no outbox table, no Debezium, no Connect cluster,
and no dual-write inconsistency window. See [docs/producing.md](docs/producing.md) for
the produce paths and when to use each.

## Status

The following all work today:

- Unmodified clients produce, consume, and rebalance: librdkafka and `kcat`, the Java
  client and its console tools, Sarama, and kafka-python.
- A default-config Java `KafkaProducer` with idempotence on (the default since Kafka
  3.0) works with no overrides.
- Admin APIs: `kafka-topics.sh`, `kafka-configs.sh`, `kafka-consumer-groups.sh`,
  `kafka-acls.sh`, transactions, share groups, and the KIP-848 consumer protocol.
- Retention reclaims disk, and `cleanup.policy=compact` topics are compacted on both
  storage engines.
- Clients authenticate with SCRAM-SHA-256 against Postgres roles or an mTLS certificate,
  with ACLs in a SQL-managed table.
- Consumers truncate rather than read divergent data when an async replica is promoted,
  verified against a real physical standby.
- The conformance suite drives four real clients against kafgres and a reference Kafka
  and diffs the observable results; it runs in CI on every pull request, and every intended
  difference is catalogued in [docs/conformance.md](docs/conformance.md).
- The segment engine (the default) passes the same conformance suite, survives `kill -9`
  with every acknowledged record intact, and replicates its log to a standby out of
  band. By default every acknowledged record also survives a host crash. On an i9-13900
  with power-loss-protected NVMe it produced about 2.4x the table engine's throughput
  with both durability settings relaxed. The strict defaults cost 3 to 25%: 806 MB/s
  relaxed against 605 MB/s strict for 1 KiB records from 4 producers (the full table is
  in [docs/configuration.md](docs/configuration.md)).
- `kafgres_produce()` commits atomically with a business write.
- CDC: a table's changes reach a topic through a logical decoding output plugin shipped
  with the extension, with the mapping written in SQL. See
  [docs/producing.md](docs/producing.md).

**If you run the segment engine, set `kafgres.segment_archive_command`.** The segment
engine's log lives in files, so `pg_basebackup` seeds a replica but is not a backup:
retention unlinks rolled segments that an archive would still want. The setting takes a
shell command with `%p`/`%f`, exactly as Postgres's own `archive_command` does, and
retention refuses to reclaim a segment the archive has not taken. As with WAL archiving,
a failing command stops reclamation and the disk grows, so watch
`kafgres_archive_status()`. The table engine needs none of this; its log is in Postgres
tables and `pg_basebackup` already covers it.

## Try it

`docker compose up -d` starts a Postgres preloaded with `kafgres` and creates the
extension on first start (`CREATE EXTENSION kafgres` runs from the image's init
scripts). On a cluster you administer yourself, add `kafgres` to
`shared_preload_libraries` and run `CREATE EXTENSION kafgres;`.

`scripts/kcat-demo.sh` then points `kcat` at it and runs the commands you would run
against any Kafka broker. It needs the broker up; with no local `kcat` it builds the
small test-client image on first use:

```
docker compose up -d
bash scripts/kcat-demo.sh
```

```
kafgres: a Kafka broker inside PostgreSQL

There is no broker process. Port 9092 is served by a Postgres background worker:

$ psql -tAc "SELECT 'PostgreSQL ' || current_setting('server_version')"
  PostgreSQL 16.14 (Debian 16.14-1.pgdg12+1)

$ psql -tAc "SELECT backend_type FROM pg_stat_activity
                   WHERE backend_type = 'kafgres_broker'"
  kafgres_broker

Topics are created in SQL, because a topic is a row:

$ psql -tAc "SELECT kafgres_create_topic('payments', 3)"
  121

Everything from here is plain kcat, pointed at 127.0.0.1:9092.

$ kcat -b 127.0.0.1:9092 -L -t payments
  Metadata for payments (from broker 1: 127.0.0.1:9092/1):
   1 brokers:
    broker 1 at 127.0.0.1:9092 (controller)
   1 topics:
    topic "payments" with 3 partitions:
      partition 0, leader 1, replicas: 1, isrs: 1
      partition 1, leader 1, replicas: 1, isrs: 1
      partition 2, leader 1, replicas: 1, isrs: 1

Produce three keyed records. The client hashes the key to a partition, so this
also checks that the broker serves the partition the client chose:

$ p