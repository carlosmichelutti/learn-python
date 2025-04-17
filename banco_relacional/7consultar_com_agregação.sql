select 
    regiao as 'Região',
    sum(população) as Total
from estados
group by regiao
order by Total desc

select 
    avg(população) as 'Média'
from estados
