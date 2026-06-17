with temps as
         (select id,
                 temperature,
                 recordDate,
                 LAG(temperature) OVER (ORDER BY recordDate) as prev_temp, LAG(recordDate) OVER (ORDER BY recordDate) as prev_date
          from weather)
select id as Id
from temps
where temperature > prev_temp
  and recordDate = prev_date + INTERVAL '1 day'