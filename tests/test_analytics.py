from sales_analytics import create_database, load_sales, monthly_revenue, segment_revenue, top_products


def test_sales_pipeline_loads_and_aggregates():
    connection = create_database()
    load_sales(connection)
    months = monthly_revenue(connection)
    assert len(months) == 4
    assert months[0] == {"month": "2024-01", "revenue": 710.0}
    assert top_products(connection)[0]["name"] == "Support Desk Pro"
    assert segment_revenue(connection)[0]["segment"] in {"startup", "enterprise"}