-- Inner join table1 and table2 on id
select * from table1 x join table2 y on x.id = y.id;

-- Inner join of table1 and table2 on id and name
select * from table1 x join table2 y on x.id = y.id and x.name = y.name;

-- Left outer join of table1 and table2 on id
select * from table1 x left join table2 y on x.id = y.id;

-- All rows that exist in table1 that do not exist in table2
select x.id, x.name from table1 x left join table2 y on x.id = y.id where y.name is null;
