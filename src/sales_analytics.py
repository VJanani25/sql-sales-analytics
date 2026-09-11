from __future__ import annotations

import csv
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def create_database(database_path: str | Path = ":memory:") -> sqlite3.Connection:
    connection = sqlite3.connect(str(database_path))
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript((ROOT / "schema.sql").read_text(encoding="utf-8"))
    return connection


def load_sales(connection: sqlite3.Connection, csv_path: str | Path = ROOT / "data/sales.csv") -> None:
    with Path(csv_path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            connection.execute(
                "INSERT OR IGNORE INTO customers(customer_id, name, segment) VALUES (?, ?, ?)",
                (row["customer_id"], row["customer_name"], row["segment"]),
            )
            connection.execute(
                "INSERT OR IGNORE INTO products(product_id, name, category, unit_price) VALUES (?, ?, ?, ?)",
                (row["product_id"], row["product_name"], row["category"], row["unit_price"]),
            )
            connection.execute(
                "INSERT OR IGNORE INTO orders(order_id, customer_id, product_id, order_date, quantity) VALUES (?, ?, ?, ?, ?)",
                (row["order_id"], row["customer_id"], row["product_id"], row["order_date"], row["quantity"]),
            )
    connection.commit()


def monthly_revenue(connection: sqlite3.Connection) -> list[dict[str, object]]:
    rows = connection.execute(
        """
        SELECT substr(o.order_date, 1, 7) AS month,
               ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
        FROM orders o JOIN products p ON p.product_id = o.product_id
        GROUP BY month ORDER BY month
        """
    ).fetchall()
    return [dict(row) for row in rows]


def top_products(connection: sqlite3.Connection) -> list[dict[str, object]]:
    rows = connection.execute(
        """
        SELECT p.name,
               ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
        FROM orders o JOIN products p ON p.product_id = o.product_id
        GROUP BY p.product_id, p.name
        ORDER BY revenue DESC
        """
    ).fetchall()
    return [dict(row) for row in rows]


def segment_revenue(connection: sqlite3.Connection) -> list[dict[str, object]]:
    rows = connection.execute(
        """
        SELECT c.segment,
               ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
        FROM orders o
        JOIN customers c ON c.customer_id = o.customer_id
        JOIN products p ON p.product_id = o.product_id
        GROUP BY c.segment
        ORDER BY revenue DESC
        """
    ).fetchall()
    return [dict(row) for row in rows]