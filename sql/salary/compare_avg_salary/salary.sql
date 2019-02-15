-- compare average department salary against average company salary
with company_sum as (
    select avg(amount) as c_avg
        , strftime('%Y-%m', pay_date) as pay_month
    from salary
    group by strftime('%Y-%m', pay_date)
),
department_sum as (
    select avg(s.amount) as d_avg
        , strftime('%Y-%m', s.pay_date) as pay_month
        , e.department_id
    from salary as s
    join employee as e
      on e.employee_id = s.employee_id
    group by strftime('%Y-%m', s.pay_date)
        , e.department_id
)
select c.pay_month
    , d.department_id
    , case when d.d_avg > c.c_avg then 'higher'
        when d.d_avg < c.c_avg then 'lower'
        else 'same'
    end as comparison
from company_sum as c
join department_sum as d
  on c.pay_month = d.pay_month
order by c.pay_month desc, d.department_id
;