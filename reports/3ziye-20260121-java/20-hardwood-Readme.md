# Hardwood

A minimal dependency parser for the Apache Parquet file format.

## Project Vision

Now:

* Be light-weight: Implement the Parquet file format avoiding any 3rd party dependencies other than for compression algorithms (e.g. Snappy)
* Be correct: Support all Parquet files which are supported by the canonical [parquet-java](https://github.com/apache/parquet-java) library

In the future:

* Be fast: As fast or faster as parquet-java
* Be complete: Add a Parquet file writer

## Set-Up

### Adding the Core Dependency

**Maven:**

```xml
<dependency>
    <groupId>dev.hardwoodhq</groupId>
    <artifactId>hardwood-core</artifactId>
    <version>1.0.0-SNAPSHOT</version>
</dependency>
```

**Gradle:**

```groovy
implementation 'dev.hardwoodhq:hardwood-core:1.0.0-SNAPSHOT'
```

### Compression Libraries

Hardwood supports reading Parquet files compressed with GZIP (built into Java), Snappy, ZSTD, LZ4, and Brotli. The compression libraries are optional dependencies—add only the ones you need:

**Maven:**

```xml
<!-- Snappy compression -->
<dependency>
    <groupId>org.xerial.snappy</groupId>
    <artifactId>snappy-java</artifactId>
    <version>1.1.10.8</version>
</dependency>

<!-- ZSTD compression -->
<dependency>
    <groupId>com.github.luben</groupId>
    <artifactId>zstd-jni</artifactId>
    <version>1.5.7-6</version>
</dependency>

<!-- LZ4 compression -->
<dependency>
    <groupId>org.lz4</groupId>
    <artifactId>lz4-java</artifactId>
    <version>1.8.1</version>
</dependency>

<!-- Brotli compression -->
<dependency>
    <groupId>com.aayushatharva.brotli4j</groupId>
    <artifactId>brotli4j</artifactId>
    <version>1.20.0</version>
</dependency>
```

**Gradle:**

```groovy
// Snappy compression
implementation 'org.xerial.snappy:snappy-java:1.1.10.8'

// ZSTD compression
implementation 'com.github.luben:zstd-jni:1.5.7-6'

// LZ4 compression
implementation 'org.lz4:lz4-java:1.8.1'

// Brotli compression
implementation 'com.aayushatharva.brotli4j:brotli4j:1.20.0'
```

If you attempt to read a file using a compression codec whose library is not on the classpath, Hardwood will throw an exception with a message indicating which dependency to add.

---

## Usage

### Row-Oriented Reading (PqRow API)

The `RowReader` provides a convenient row-oriented interface for reading Parquet files. The `PqRow` API provides typed accessor methods for type-safe field access.

```java
import dev.morling.hardwood.reader.ParquetFileReader;
import dev.morling.hardwood.reader.RowReader;
import dev.morling.hardwood.row.PqRow;
import dev.morling.hardwood.row.PqList;
import dev.morling.hardwood.row.PqIntList;
import dev.morling.hardwood.row.PqMap;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalTime;
import java.math.BigDecimal;
import java.util.UUID;

try (ParquetFileReader fileReader = ParquetFileReader.open(path)) {
    try (RowReader rowReader = fileReader.createRowReader()) {
        for (PqRow row : rowReader) {
            // Access columns by name with typed accessors
            long id = row.getLong("id");
            String name = row.getString("name");

            // Logical types are automatically converted
            LocalDate birthDate = row.getDate("birth_date");
            Instant createdAt = row.getTimestamp("created_at");
            LocalTime wakeTime = row.getTime("wake_time");
            BigDecimal balance = row.getDecimal("balance");
            UUID accountId = row.getUuid("account_id");

            // Check for null values
            if (!row.isNull("age")) {
                int age = row.getInt("age");
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
            }

            // Access nested structs
            PqRow address = row.getRow("address");
            if (address != null) {
                String city = address.getString("city");
                int zip = address.getInt("zip");
            }

            // Access lists and iterate with typed accessors
            PqList tags = row.getList("tags");
            if (tags != null) {
                for (String tag : tags.strings()) {
                    System.out.println("Tag: " + tag);
                }
            }

            // Access list of structs
            PqList contacts = row.getList("contacts");
            if (contacts != null) {
                for (PqRow contact : contacts.rows()) {
                    String contactName = contact.getString("name");
                    String phone = contact.getString("phone");
                }
            }

            // Access nested lists (list<list<int>>) using primitive int lists
            PqList matrix = row.getList("matrix");
            if (matrix != null) {
                for (PqIntList innerList : matrix.intLists()) {
                    for (var it = innerList.iterator(); it.hasNext(); ) {
                        int val = it.nextInt();
                        System.out.println("Value: " + val);
     