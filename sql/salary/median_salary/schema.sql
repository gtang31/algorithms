.headers on
.mode column
create table salary (id integer, company text, salary integer);
insert into salary (id, company, salary)
    values (1, 'A', 2341)
    , (2, 'A', 341)
    , (3, 'A', 15)
    , (4, 'A', 15314)
    , (5, 'A', 451)
    , (6, 'A', 513)
    , (7, 'B', 15)
    , (8, 'B', 13)
    , (9, 'B', 1154)
    , (10, 'B', 1345)
    , (11, 'B', 1221)
    , (12, 'B', 234)
    , (13, 'C', 2345)
    , (14, 'C', 2645)
    , (15, 'C', 2645)
    , (16, 'C', 2652)
    , (17, 'C', 65);


create table salary_frequency (salary integer, frequency integer);
insert into salary_frequency (salary, frequency)
    values (55000, 7)
        , (90000, 1)
        , (70000, 3)
        , (40000, 1);