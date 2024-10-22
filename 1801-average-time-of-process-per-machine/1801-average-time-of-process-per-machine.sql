/* Write your T-SQL query statement below */
select machine_id, round(avg(end_time - start_time),3) as processing_time
from
(
select machine_id,process_id,
    min(case when activity_type = 'start' then timestamp end) as start_time,
    max(case when activity_type = 'end' then timestamp end) as end_time
    from activity
    group by machine_id,process_id
) as t
group by machine_id