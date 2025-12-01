# PostgreSQL AI Query Extension

A powerful PostgreSQL extension that generates SQL queries from natural language using state-of-the-art AI models from OpenAI and Anthropic.

## Features

- **Natural Language to SQL**: Convert plain English descriptions into valid PostgreSQL queries
- **Available OpenAI Models:**

You can use any valid OpenAI model name. Here is a comparison of common models:

| Model Name | Type | Cost | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| `gpt-5` | Next Gen | High | Ultimate reasoning and capabilities | High cost, availability limited |
| `gpt-4o` | Flagship | Moderate | Best overall performance, fast | Higher cost than mini |
| `gpt-4o-mini` | Economy | Low | Very cheap, fast, good for simple tasks | Less capable reasoning than 4o |


- **Automatic Schema Discovery**: Analyzes your database schema to understand table structures and relationships
- **Intelligent Query Generation**: Creates optimized queries with appropriate JOINs, WHERE clauses, and LIMIT constraints
- **Query Performance Analysis**: Run EXPLAIN ANALYZE on queries and get AI-powered performance insights and optimization suggestions
- **Configurable Response Formatting**: Choose between plain SQL, enhanced text with explanations, or structured JSON responses
- **Safety First**: Built-in protections against dangerous operations and unauthorized system table access
- **Flexible Configuration**: File-based configuration with support for API keys, model selection, and response formatting

## Quick Start

### Installation

1.  **Prerequisites**:
    - PostgreSQL 12+ with development headers
    - CMake 3.16+
    - C++20 compatible compiler
    - API key from OpenAI or Anthropic

2.  **Build and Install**:
    ```bash
    git clone --recurse-submodules https://github.com/benodiwal/pg_ai_query.git
    cd pg_ai_query
    mkdir build && cd build
    cmake ..
    make && sudo make install
    ```

3.  **Enable Extension**:
    ```sql
    CREATE EXTENSION pg_ai_query;
    ```

### Configuration

Create `~/.pg_ai.config`:

```ini
[general]
log_level = "INFO"
enable_logging = false

[query]
enforce_limit = true
default_limit = 1000

[response]
show_explanation = true
show_warnings = true
show_suggested_visualization = false
use_formatted_response = false

[openai]
api_key = "your-openai-api-key-here"
default_model = "gpt-4o"

[anthropic]
api_key = "your-anthropic-api-key-here"
default_model = "claude-3-5-sonnet-20241022"
```

### Environment Variables

You can also configure API keys using environment variables. These will override values in the configuration file:

- `OPENAI_API_KEY`: API key for OpenAI
- `ANTHROPIC_API_KEY`: API key for Anthropic

Example:
```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Available Anthropic Models:**

You can use any valid Anthropic model name. Here is a comparison of common models:

| Model Name | Type | Cost | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| `claude-4.5-opus` | Next Gen | High | Ultimate reasoning and capabilities | High cost, availability limited |
| `claude-sonnet-4-5-20250929` | Flagship | Moderate | Top-tier reasoning and coding | - |
| `claude-3-haiku-20240307` | Economy | Low | Extremely fast and cheap | Lower reasoning capability |

### Basic Usage

```sql
-- Generate simple queries
SELECT generate_query('show all customers');

-- Generate complex analytical queries
SELECT generate_query('monthly sales trend for the last year by category');

-- Generate queries with business logic
SELECT generate_query('customers who have not placed orders in the last 6 months');

-- Schema discovery functions
SELECT get_database_tables();
SELECT get_table_details('orders');

-- Explain and analyze query performance
SELECT explain_query('SELECT * FROM users WHERE created_at > NOW() - INTERVAL ''7 days''');
SELECT explain_query('SELECT u.name, COUNT(o.id) FROM users u LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id');
```

### Response Formats

**Plain SQL (default)**:
```sql
SELECT * FROM customers WHERE created_at >= NOW() - INTERVAL '7 days' LIMIT 1000;
```

**Enhanced with explanations and warnings**:
```sql
SELECT * FROM customers WHERE created_at >= NOW() - INTERVAL '7 days' LIMIT 1000;

-- Explanation:
-- Retrieves all customers who were created within the last 7 days

-- Warnings:
-- 1. Large dataset: Consider adding specific filters for better performance
```

**JSON format** (set `use_formatted_response = true`):
```json
{
  "query": "SELECT * FROM customers WHERE created_at >= NOW() - INTERVAL '7 days' LIMIT 1000;",
  "success": true,
  "explanation": "Retrieves all customers who were created within the last 7 days",
  "warnings": ["Large dataset: Consider adding specific filters for better performance"],
  "suggested_visualization": "table",
  "row_limit_applied": true
}
```

### Query Performance Analysis

The `explain_query` function runs EXPLAIN ANALYZE on your queries and provides AI-generated performance insights:

