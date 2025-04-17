update estados 
set nome = 'Maranhão'
where sigla = 'MA'

select nome from estados where sigla = 'MA'

update estados 
set nome = 'Paraná', população = 11.32
where sigla = 'PR'

select * from estados where sigla = 'PR'