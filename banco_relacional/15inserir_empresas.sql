insert into empresas (nome, cnpj)
values
    ('Brasesco', 210049120),
    ('Vale', 03490340239),
    ('Cielo', 2342142342)

alter table empresas modify cnpj varchar(20) 

desc empresas;
desc prefeitos;
select * from empresas;
select * from cidades;

insert into empresas_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)