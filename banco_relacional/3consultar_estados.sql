select * from estados

select nome as 'Nome do Estado', sigla as 'Sigla', regiao as 'Região' from estados 

select * from estados 
where regiao = 'Sudeste'

select nome, regiao, população from estados 
where população >= 10
order by população desc