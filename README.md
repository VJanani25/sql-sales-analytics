# SQL Sales Analytics

A reproducible SQLite analytics project that turns a small sales CSV into decision-ready business summaries. It demonstrates schema design, data loading, joins, aggregation, filtering, and a concise reporting workflow without hiding the SQL behind a dashboard framework.

## Business questions

- Which products generate the most revenue?
- Which categories are growing?
- What is the monthly revenue trend?
- Which customers contribute the most value?

## Features

- Normalized SQLite schema for customers, products, and orders
- Deterministic CSV seed data
- Separate SQL query file for review
- Monthly revenue and top-product reports
- Python runner for repeatable execution
- Tests for schema loading and analytical outputs

## Technology

- Python 3.10+
- SQLite
- SQL
- Python `csv` and `sqlite3` standard-library modules
- `pytest` for tests

## Run

```bash
cd sql-sales-analytics
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_report.py
```

Example output:

```text
Monthly revenue
2024-01: 540.00
2024-02: 760.00

Top products
Analytics Starter: 720.00
Support Desk Pro: 580.00
```

## Test

```bash
PYTHONPATH=src python -m pytest
```

## Workflow

```text
data/sales.csv
     │
     ▼
schema.sql + load_csv()
     │
     ▼
SQLite database
     │
     ▼
queries.sql
     │
     ▼
business summary
```

## Future improvements

- Add date-range and customer-segment filters
- Export reports to CSV and charts
- Add data-quality checks for duplicate orders
- Schedule the report in CI
- Replace the fixture with a documented production extract

## Resume bullet

Designed a normalized SQLite sales model and wrote reproducible SQL analytics for monthly revenue, customer value, and product performance using Python data-loading scripts.

## Author

Janani Varadharajan