-- Write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive)
-- use self cross join
select a.id
    , a.date
    , a.people
from stadium as a, stadium as b, stadium as c
where (c.id-b.id = 1 and b.id-a.id = 1)  -- start
  or (a.id-b.id = 1 and b.id-c.id = 1)  -- middle
  or (a.id-b.id = 1 and c.id-a.id = 1))  -- end
  and (a.people >= 100 and b.people >= 100 and c.people >= 100)
group by a.id
    , a.date
    , a.people
order by a.id
;