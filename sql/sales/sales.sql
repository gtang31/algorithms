--a. The names of all salespeople that have an order with Samsonic. 
select s.name
from Salesperson as s
join Orders as o
  on s.id = o.salesperson_id
join Customer as c
  on c.id = o.customer_id
where c.name = "Samsonic";

--b. The names of all salespeople that do not have any order with Samsonic.
select distinct s.name
from Salesperson as s
join Orders as o
  on s.id = o.salesperson_id
join Customer as c
  on c.id = o.customer_id
where c.name != "Samsonic";

--c. The names of salespeople that have 2 or more orders.
select s.name
  , count(s.name)
from Salesperson as s
join Orders as o
  on s.id = o.salesperson_id
group by s.name
having count(s.name) > 1;

--d. The names and ages of all salespersons must having a salary of 100,000 or greater.
select s.name
  , s.age
from Salesperson as s
where s.salary >= 100000;

--e. What sales people have sold more than 1400 total units?
select s.name, sum(amount)
from Salesperson as s
join Orders as o
  on s.id = o.salesperson_id
group by s.name
having sum(o.amount) > 1400;

--f. When was the earliest and latest order made to Samony?
select min(o.order_date)
    , max(o.order_date)
from Orders as o
where customer_id = 6;

--g. Find the largest order amount for each salesperson and the associated order number, along with the customer to whom that order belongs to
select s.id
  , t.max_amount
  , o.customer_id
from Salesperson as s
join (
    select o.salesperson_id
      , max(o.amount) as max_amount
    from Orders as o
    group by o.salesperson_id
) as t
  on s.id = t.salesperson_id
join Orders as o
  on o.salesperson_id = t.salesperson_id
  and o.amount = t.max_amount;
