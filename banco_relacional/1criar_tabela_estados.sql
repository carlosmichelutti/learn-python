create table estados(
    id int unsigned not null auto_increment,
    nome varchar(45) not null,
    sigla varchar(2) not null,
    regiao enum('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'),
    população decimal(5, 2) not null,
    primary key(id),
    unique key (id),
    unique key (nome)
)