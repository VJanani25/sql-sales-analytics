-- Monthly revenue
SELECT substr(o.order_date, 1, 7) AS month,
       ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
FROM orders o
JOIN products p ON p.product_id = o.product_id
GROUP BY month
ORDER BY month;

-- Top products by revenue
SELECT p.name,
       ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
FROM orders o
JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_id, p.name
ORDER BY revenue DESC;

-- Revenue by customer segment
SELECT c.segment,
       ROUND(SUM(o.quantity * p.unit_price), 2) AS revenue
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN products p ON p.product_id = o.product_id
GROUP BY c.segment
ORDER BY revenue DESC;