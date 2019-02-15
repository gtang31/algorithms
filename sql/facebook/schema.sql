.headers on
.mode column
create table user_login (session_id integer primary key
    , user_id integer not null
    , login_ts text not null
    , logout_ts text not null
);
insert into user_login (session_id, user_id, login_ts, logout_ts)
    values (null, 1, '2018-09-26', '2018-09-26')
        , (null, 1, '2018-09-27', '2018-09-27')
        , (null, 1, '2018-09-28', '2018-09-28')
        , (null, 1, '2018-09-29', '2018-09-29')
        , (null, 1, '2018-09-30', '2018-09-30')
        , (null, 1, '2018-10-01', '2018-10-01')
        , (null, 1, '2018-10-02', '2018-10-02')
        , (null, 1, '2018-10-03', '2018-10-03')
        , (null, 1, '2018-10-04', '2018-10-04')
        , (null, 2, '2018-09-08', '2018-09-08')
        , (null, 2, '2018-09-18', '2018-09-19')
        , (null, 2, '2018-09-29', '2018-09-29')
        , (null, 3, '2018-09-20', '2018-09-21')
        , (null, 3, '2018-09-26', '2018-09-26')
        , (null, 3, '2018-09-26', '2018-09-26')
        , (null, 3, '2018-09-27', '2018-09-27')
        , (null, 3, '2018-09-28', '2018-09-28')
        , (null, 4, '2018-09-28', '2018-09-28')
        , (null, 4, '2018-09-28', '2018-09-28')
        , (null, 5, '2018-09-20', '2018-09-28')
        , (null, 5, '2018-09-27', '2018-09-28')
        , (null, 5, '2018-09-29', '2018-09-29')
        , (null, 6, '2018-10-01', '2018-10-02')
        , (null, 6, '2018-10-02', '2018-10-02')
        , (null, 7, '2018-09-20', '2018-09-20')
        , (null, 8, '2018-09-14', '2018-09-15')
        , (null, 9, '2018-09-28', '2018-09-28')
        , (null, 9, '2018-10-03', '2018-10-04')
        , (null, 10, '2018-10-05', '2018-10-05')
;

/* Practice querying for:
    1.) whole path(s) and whole tree
    2.) leaf and intermediate nodes
    3.) inserting nodes
    4.) updating node lft, rgt values
The `lft` and `rgt` values are determined by a preorder tree traversal
*/
-- create adjacency list
CREATE TABLE nested_category (
        category_id integer PRIMARY KEY,
        name text NOT NULL,
        lft integer NOT NULL,
        rgt integer NOT NULL
);
INSERT INTO nested_category (category_id, name, lft, rgt)
    VALUES (1, 'ELECTRONICS', 1, 20)
    , (2, 'TELEVISIONS', 2, 9)
    , (3, 'TUBE', 3, 4)
    , (4, 'LCD', 5, 6)
    , (5, 'PLASMA', 7, 8)
    , (6, 'PORTABLE ELECTRONICS', 10, 19)
    , (7, 'MP3 PLAYERS', 11, 14)
    , (8, 'FLASH', 12, 13)
    , (9, 'CD PLAYERS', 15, 16)
    , (10, '2 WAY RADIOS', 17, 18)
;
