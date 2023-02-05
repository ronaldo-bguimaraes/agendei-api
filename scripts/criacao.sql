drop table if exists usuario;

create table usuario (
	id_usuario int unsigned not null auto_increment,
	primary key (id_usuario)
);

select * from usuario;

drop table if exists prestador;

create table prestador (
	id_prestador int unsigned not null auto_increment,
	id_usuario int unsigned not null,
	primary key (id_prestador),
	foreign key (id_usuario) references usuario(id_usuario)
);

select * from prestador;

drop table if exists servico;

create table servico (
	id_servico int unsigned not null auto_increment,
	nome varchar(50) not null,
	descricao varchar(200) not null,
	valor_servico decimal(6,2) not null,
	duracao time not null,
	id_prestador int unsigned not null,
	primary key (id_servico),
	foreign key (id_prestador) references prestador(id_prestador)
);