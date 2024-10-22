/* Write your T-SQL query statement below */

select 
    p.product_id,
    isnull(round(cast(sum(p.price*s.units)as float)/sum(s.units),2),0) as average_price
from 
    prices as p
left join
    unitssold as s
on 
    p.product_id = s.product_id
and
    s.purchase_date between p.start_date and p.end_date
group by
    p.product_id

