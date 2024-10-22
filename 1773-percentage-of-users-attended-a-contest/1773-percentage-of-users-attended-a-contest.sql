/* Write your T-SQL query statement below */

select 
	contest_id,
	round(cast(count(user_id) as float)/(select count(*) from Users)*100,2) as percentage
from 
	Register
group by
	contest_id
ORDER BY
    percentage desc, contest_id
    


