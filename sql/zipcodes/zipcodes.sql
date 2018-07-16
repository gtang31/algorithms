-- Practice create tables, copy, alter, update, insert, de-dupes
-- Create table for zip codes
create table zipcodes(
    id integer primary key not null auto_increment
    , zip char(5) not null
    , city varchar(50)
    , state varchar(20)
    , state_abbrv char(2)
    , county varchar(30)
    , latitude numeric(6,4)
    , longitude numeric(7,4));
    
