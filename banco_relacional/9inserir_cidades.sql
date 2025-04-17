insert into cidades (nome, área, estado_id)
values ("Sertãozinho", 2000, (select id from estados where sigla = 'SP'))

insert into cidades (nome, área, estado_id)
values ("Ribeirão Preto", 5000, (select id from estados where sigla = 'SP'))

insert into cidades (nome, área, estado_id)
values ('Caruaru', 920.6, (select id from estados where sigla = 'PE'))

insert into cidades (nome, área, estado_id)
values ('Juazeiro do Norte', 248.2, (select id from estados where sigla = 'CE'))

select * from cidades



