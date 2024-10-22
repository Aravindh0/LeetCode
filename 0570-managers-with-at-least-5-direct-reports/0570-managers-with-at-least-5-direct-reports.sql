/* Write your T-SQL query statement below */
select em.name from employee em
inner join employee as e
on em.id = e.managerID
group by em.name, em.id
having count(e.managerID) >=5

