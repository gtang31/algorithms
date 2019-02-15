.headers on
.mode column
CREATE TABLE Departments(id integer primary key, Name text not null);
insert into Departments (id, Name)
    values (1, "Engineering")
    , (2, "Sales")
    , (3, "Marketing")
    , (4, "Finance")
    , (5, "Customer Solutions")
    , (6, "Ops");
CREATE TABLE Employees(id integer primary key
    , DepartmentId integer
    , BossId integer
    , Name text not null
    , Salary integer not null);
insert into Employees (id, DepartmentId, BossId, Name, Salary)
    values (1, 4, null, "Justin", 2000000)
    , (2, 1, 3, "Gary", 130000)
    , (3, 1, 4, "Nick", 150000)
    , (4, 1, 1, "Henrik", 200000)
    , (5, 4, 1, "Vito", 60000)
    , (6, 4, 5, "Karishma", 65000)
    , (7, 1, 4, "DLee", 170000)
    , (8, 3, 1, "Lena", 100000)
    , (9, 2, 1, "Gottleib", 200000)
    , (10, 2, 9, "Dane", 100000)
    , (11, 5, 1, "Kathy", 180000)
    , (12, 5, 11, "Ben", 130000)
    , (13, 5, 12, "Greg", 90000)
    , (14, 1, 4, "Sebastian", 150000)
;