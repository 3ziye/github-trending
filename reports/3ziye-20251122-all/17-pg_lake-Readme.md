# pg_lake: Postgres for Iceberg and Data lakes

`pg_lake` integrates Iceberg and data lake files into Postgres. With the `pg_lake` extensions, you can use Postgres as a stand-alone lakehouse system that supports transactions and fast queries on Iceberg tables, and can directly work with raw data files in object stores like S3.

At a high level, `pg_lake` lets you:

- **Create and modify [Iceberg](https://iceberg.apache.org/)** tables directly from PostgreSQL, with full transactional guarantees and query them from other engines
- **Query and import data files in object storage** in [Parquet](https://parquet.apache.org/), CSV, JSON, and Iceberg format
- **Export query results back to object storage** in Parquet, CSV, or JSON formats using COPY commands
- **Read geospatial formats** supported by GDAL, such as GeoJSON and Shapefiles
- **Use the built-in [map type](./pg_map/README.md)** for semi-structured or key–value data  
- **Combine heap, Iceberg, and external Parquet/CSV/JSON** files in the same SQL queries and modifications — all with full transactional guarantees and no SQL limitations  
- **Infer table columns and types** from external data sources such as Iceberg, Parquet, JSON, and CSV files
- **Leverage DuckDB’s query engine** underneath for fast execution without leaving Postgres  

## Setting up `pg_lake`

There are two ways to set up `pg_lake`:  
- **Using Docker**, for an easy, ready-to-run test environment.  
- **Building from source**, for a manual setup or development use.  

Both approaches include the PostgreSQL extensions, the `pgduck_server` application and setting up S3-compatible storage.

### Using Docker

Follow the [Docker README](./docker/README.md) to set up and run `pg_lake` with Docker.


### Building from source

Once you’ve [built and installed the required components](./docs/building-from-source.md), you can initialize `pg_lake` inside Postgres.

#### Creating the extensions

Create all required extensions at once using `CASCADE`:

```sql
CREATE EXTENSION pg_lake CASCADE;
NOTICE:  installing required extension "pg_lake_table"
NOTICE:  installing required extension "pg_lake_engine"
NOTICE:  installing required extension "pg_extension_base"
NOTICE:  installing required extension "pg_lake_iceberg"
NOTICE:  installing required extension "pg_lake_copy"
CREATE EXTENSION
```

#### Running `pgduck_server`

`pgduck_server` is a standalone process that implements the Postgres wire-protocol (locally), and underneath uses `DuckDB` to execute queries.

When you run `pgduck_server` it starts listening to port `5332` on unix domain socket:
```
pgduck_server
LOG pgduck_server is listening on unix_socket_directory: /tmp with port 5332, max_clients allowed 10000
```

As `pgduck_server` implements Postgres wire protocol, you can access it via `psql` on port `5332` and host `/tmp` and run commands via DuckDB. 

For example, you can get the DuckDB version:

```sql
psql -p 5332 -h /tmp

select version() as duckdb_version; 
duckdb_version 
---------------- 
v1.3.2 (1 row)
```

You can also provide some additional settings while starting the server, to see all:
```
pgduck_server --help
```

There are some important settings that should be adjusted, especially on production systems:


- `--memory_limit`: Optionally specify the maximum memory of pgduck_server similar to DuckDB's memory_limit, the default is 80 percent of the system memory
- `--init_file_path <path>`: Execute all statements in this file on start-up
- `--cache_dir`: Specify the directory to use to cache remote files (from S3)

Note that if you want to make adjustments to duckdb settings, you can use the `--init_file_path` approach OR you can
connect to the running pgduck_server and make changes. For example:

```
$ psql -h /tmp -p 5332
psql (17.5, server 16.4.DuckPG)
Type "help" for help.

postgres=> set global threads = 16;
SET
```

The connection above is to the pgduck_server on its port (default 5332), NOT to the postgres/pg_lake server. 


#### Connecting `pg_lake` to s3 (or compatible)

`pgduck_server` relies on the DuckDB [secrets manager](https://duckdb.org/docs/stable/configuration/secrets_manager) for credentials and it follows the credentials chain by default for AWS and GCP. Make sure your cloud credentials are configured properly — for example, by setting them in ~/.aws/credentials.  

Once you set up the credential chain, you should set the `pg_lake_iceberg.default_location_prefix`. This is the location where Iceberg tables are stored:

```sql
SET pg_lake_iceberg.default_location_prefix TO 's3://testbucketpglake';
```

You can also set the credentials on `pgduck_server` for [local development with `minio`](docs/building-from-source.md#running-s3-compatible-service-minio-locally).

## Using pg_lake

### Create an Iceberg table

You can create Iceberg tables by adding `USING iceberg` to your `CREATE TABLE` statements.

```sql
CREATE TABLE iceberg_test USING iceberg 
      AS SELECT 
            i as key, 'val_'|| i  as val
    