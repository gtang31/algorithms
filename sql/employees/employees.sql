-- Tables referenced in here can be found in Employees.db
-- CREATE TABLE Departments(DepartmentId integer primary key, Name text not null);
-- CREATE TABLE Employees(EmployeeId integer primary key, DepartmentId integer, BossId integer not null, Name text not null, Salary integer not null);

-- Questions:
-- List employees (names) who have a bigger salary than their boss
select x.EmployeeId, x.BossId, x.Salary, x.Name, y.Name from Employees x join Employees y on x.BossId = y.EmployeeId where y.Salary < x.Salary;

--List employees who have the biggest salary in their departments
select x.Name, y.Name, max(x.Salary) from Employees x join Departments y on x.DepartmentId = y.DepartmentId group by y.Name order by x.EmployeeId;

--List departments that have less than 3 people in it
select y.Name, count(x.Name) from Departments y left join Employees x on x.DepartmentId = y.DepartmentId group by y.Name having count(x.Name) < 3;

--List all departments along with the number of people there (tricky - people often do an "inner join" leaving out empty departments)
select y.Name, count(x.Name) from Departments y left join Employees x on x.DepartmentId = y.DepartmentId group by y.Name;

--List employees that don't have a boss in the same department
select x.Name, z.Name, y.Name from Employees x join Employees y on x.BossId = y.EmployeeId join Departments z on x.DepartmentId = z.DepartmentId where x.DepartmentId != y.DepartmentId;

--List all departments along with the total salary there
select x.DepartmentId, y.Name, sum(x.Salary) from Employees x join Departments y on x.DepartmentId = y.DepartmentId group by y.Name order by 1;
