-- find the 3 month cumulative salary
-- think of a sliding window, use self join
select A.Id
  , max(B.Month) as Month
  , sum(B.Salary) as '3 Month Cumulative Salary'
from Employee as A
cross join Employee as B
where A.Id = B.Id
  -- three month window
  and B.Month >= A.Month-3
  and B.Month <= A.Month-1
group by A.Id
    , A.Month
order by A.Id, A.Month, B.Salary;