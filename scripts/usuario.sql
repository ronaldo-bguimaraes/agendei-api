-- name: drop
drop table if exists usuario;

-- name: create
create table usuario (
    id_usuario int unsigned not null auto_increment,
    primary key (id_usuario)
);

-- name: insert
insert into usuario values ();