-- last seven logins
select *
from (
    select user_id, max(login_ts) as most_recent_login
    from user_login
    group by user_id
) as x
left join user_login as y
  on y.login_ts > date(x.most_recent_login, '-7 day')
  and x.user_id = y.user_id;


-- running sum of 7 day active users
select t1.user_id
    , t1.login_ts
    , t2.user_id
    , t2.login_ts
from user_login as t1
join user_login as t2
  on t1.user_id = t2.user_id
where t1.login_ts >= date('2018-10-04', '-6 day')
  and (t2.login_ts >= t1.login_ts and t2.login_ts <= '2018-10-04')
order by t2.login_ts, t1.user_id;


select t1.login_ts
    -- , t2.user_id
    -- , t2.login_ts
    , sum(distinct t1.user_id) as cumsum
from user_login as t1
join user_login as t2
  on t1.user_id = t2.user_id
where t2.login_ts >= date('2018-10-04', '-6 day')
  and t2.login_ts <= t1.login_ts
-- order by t1.user_id, t1.login_ts;
group by t1.login_ts;


select 
    o.user_id, 
    o.date,
    case
        when sum(i.num_logins) >= 1 then TRUE
        else FALSE 
    end as active
from userActivityTable as o
join userActivityTable as i on 
    i.date <= o.date AND
    i.date >= (o.date :: date) - integer '7' AND
    i.user_id = o.user_id
group by o.user_id, o.date;


/* hierarchy stuff */
-- 1.) Get any path with starting point
select t2.name
from nested_category as t1
join nested_category as t2
  on (t2.lft >= t1.lft and t2.rgt <= t1.rgt)
where t1.name = 'ELECTRONICS' -- change t1.name to start path
; 

-- 2.) Get any path with ending point
select t1.name
from nested_category as t1
join nested_category as t2
  on t2.lft >= t1.lft and t2.rgt <= t1.rgt
where t2.name = 'FLASH'  -- change t2.name to end path
;

-- 3.) Get leaf nodes
select *
from nested_category
where rgt = lft+1;

-- 4.) Calculating depth of each node (essentially rank)
select t2.name
    , count(distinct t1.name)-1 as depth
from nested_category as t1
join nested_category as t2
  on (t2.lft >= t1.lft and t2.rgt <= t1.rgt)
group by t2.name
order by count(distinct t1.name);

-- 5.) Find direct children of a node



/*
For each genre in the dataset- how many genres the movies in that genre are in, on average.
For example, if an average Horror movie is in 1.3 genres and average Adventure movie is
in 2.9 genres then we would say Horror is a better-defined genre than Adventure.
To polish up your answer, please provide both the average and maximum number of genres for
movies in each genre but sort the list in descending order by average genre count.
*/ 
SELECT g.name
   --, gm.movie_id
   , avg(genre_counts.cnt) as avg_genres
FROM genres as g
join genres_movies as gm
  on g.id = gm.genre_id
join (
  select movie_id
    , count(genre_id) as cnt
  from genres_movies
  group by movie_id
) as genre_counts
  on genre_counts.movie_id = gm.movie_id
group by g.name  
order by g.name


