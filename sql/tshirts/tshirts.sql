-- Transpose a table

select name,
  sum(case when color = 'Red' then value else 0 end) Red,
  sum(case when color = 'Green' then value else 0 end) Green,
  sum(case when color = 'Blue' then value else 0 end) Blue
from(
    select color, Paul value, 'Paul' name
      from tshirts
      union all
      select color, John value, 'John' name
      from tshirts
      union all
      select color, Tim value, 'Tim' name
      from tshirts
      union all
      select color, Eric value, 'Eric' name
      from tshirts) src
group by name
