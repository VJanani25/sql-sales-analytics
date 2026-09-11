from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from sales_analytics import create_database, load_sales, monthly_revenue, segment_revenue, top_products


if __name__ == "__main__":
    connection = create_database("sales.db")
    load_sales(connection)
    print("Monthly revenue")
    for row in monthly_revenue(connection):
        print(f"{row['month']}: {row['revenue']:.2f}")
    print("\nTop products")
    for row in top_products(connection):
        print(f"{row['name']}: {row['revenue']:.2f}")
    print("\nRevenue by segment")
    for row in segment_revenue(connection):
        print(f"{row['segment']}: {row['revenue']:.2f}")