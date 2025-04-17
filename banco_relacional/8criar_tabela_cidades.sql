create table if not exists cidades(
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    estado_id int unsigned not null,
    área decimal(10, 2),
    primary key (id),
    foreign key (id) references estados(id)
)