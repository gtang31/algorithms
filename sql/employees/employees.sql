-- Questions:
-- List employees (names) who have a bigger salary than their boss
select x.id
  , x.BossId
  , x.Salary
  , x.Name
  , y.Name
from Employees x
join Employees y
  on x.BossId = y.id
where y.Salary < x.Salary;

--List employees who have the biggest salary in their departments
select x.Name
  , y.Name
  , max(x.Salary)
from Employees x
join Departments y
  on x.DepartmentId = y.id
group by y.Name
order by x.id;

--List departments that have less than 3 people in it
select y.Name
  , count(x.Name)
from Departments y
left join Employees x
  on x.DepartmentId = y.id
group by y.Name
having count(x.Name) < 3;

--List all departments along with the number of people there (tricky - people often do an "inner join" leaving out empty departments)
select y.Name
  , count(x.Name)
from Departments y
left join Employees x
  on x.DepartmentId = y.id
group by y.Name;

--List employees that don't have a boss in the same department
select x.Name
  , z.Name
  , y.Name
from Employees x
join Employees y
  on x.BossId = y.id
join Departments z
  on x.DepartmentId = z.id
where x.DepartmentId != y.DepartmentId;

--List all departments along with the total salary there
select x.DepartmentId
  , y.Name
  , sum(x.Salary)
from Employees x
join Departments y
  on x.DepartmentId = y.id
group by y.Name
order by 1;

-- dense rank employees based on their salary
select x.name
  , x.salary
  , t.dense_rank
from Employees as x
left join (
  -- count all t2.salary less than t1.salary
  select t1.salary
    , count(distinct t2.salary) as dense_rank
  from Employees as t1
  join Employees as t2
    on t2.salary >= t1.salary
  group by t1.salary
) as t
  on x.salary = t.salary
order by t.dense_rank;

-- find top three salaried employee for each department
-- implement rank


select t1.salary
  , d.Name as DepartmentName
  , count(distinct t2.salary)
from Employees as t1
join Employees as t2
  on t2.salary >= t1.salary
  and t1.DepartmentId = t2.DepartmentId
join Departments as d
  on d.Id = t1.DepartmentId
group by t1.salary, d.Name
order by DepartmentName, t1.salary;



select d.Name as Department
  , y.Employee
  , y.Salary
from (
    select x.Name as Employee
      , x.Salary
      , x.DepartmentId
      , rank as top_three
    from (
      select *
      from Employees
      order by DepartmentId
        , Salary desc
      ) as x
    where c <= 3
    order by x.DepartmentId, c
) as y
join Departments as d
  on d.Id = y.DepartmentId
;

