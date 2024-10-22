# Write your MySQL query statement below
  

SELECT 
    ROUND((SUM(CASE 
              WHEN d.order_date = d.customer_pref_delivery_date THEN 1 
              ELSE 0 
          END) * 100.0) / COUNT(DISTINCT d.customer_id),2) AS immediate_percentage
FROM 
    Delivery d
WHERE 
    d.order_date = (
        SELECT MIN(order_date)
        FROM Delivery AS d2
        WHERE d.customer_id = d2.customer_id
    );
