create table Salesperson (id smallint, name char(10), age smallint, salary int);
insert into Salesperson (id, name, age, salary)
    values (1, "Abe", 61, 140000)
    , (2, "Bob", 34, 44000)
    , (5, "Chris", 34, 40000)
    , (7, "Dan", 41, 52000)
    , (8, "Ken", 57, 115000)
    , (11, "Joe", 38, 38000);
create table Customer (id smallint, name char(20), city char(20), industry char(1));
insert into Customer (id, name, city, industry)
    values (4, "Samsonic", "Pleasanton", "J")
    , (6, "Panasung", "Oakland", "J")
    , (7, "Samony", "Jackson", "B")
    , (9, "Orange", "Jackson", "B");
create table Orders (order_number smallint, order_date date, customer_id smallint, salesperson_id smallint, amount smallint);
insert into Orders (order_number, order_date, customer_id, salesperson_id, amount)
    values (10, "1996-08-02", 4, 2, 540)
    , (20, "1999-01-30", 4, 8, 1800)
    , (30, "1995-07-14", 9, 1, 460)
    , (40, "1998-01-29", 7, 2, 2400)
    , (50, "1998-02-03", 6, 7, 600)
    , (60, "1998-03-02", 6, 7, 720)
    , (70, "1998-05-06", 9, 7, 150);