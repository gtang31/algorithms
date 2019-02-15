.headers on
.mode column
create table salary (id integer, employee_id integer, amount integer, pay_date text);
insert into salary (id, employee_id, amount, pay_date)
    values (1, 1, 9000, '2017-03-31')
    , (2, 2, 6000, '2017-03-31')
    , (3, 3, 10000, '2017-03-31')
    , (4, 1, 7000, '2017-02-28')
    , (5, 2, 6000, '2017-02-28')
    , (6, 3, 8000, '2017-02-28')
;

create table employee (employee_id integer, department_id integer);
insert into employee (employee_id, department_id)
    values (1, 1)
        , (2, 2)
        , (3, 2)
;