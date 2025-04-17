select e.nome, c.nome, e.regiao from estados as e, cidades as c
where e.id = c.estado_id

select 
    e.nome as Estado,
    c.nome as Cidade,
    e.regiao as 'Nome da Região'
from estados as e, cidades as c
where e.id = c.estado_id

select
    c.nome as Cidade, 
    e.nome as Estado, 
    regiao as Região 
from estados e
inner join cidades as c on e.id = c.estado_id