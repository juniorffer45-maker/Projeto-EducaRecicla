create table usuario (
	id int generated always as identity,
	id_localidade int,
	nome_completo varchar(100) not null,
	email varchar (100) not null unique,
	senha varchar(255) not null,
	biografia text,
	foto_perfil_url varchar(500),
	data_cadastro timestamp default current_timestamp,
	telefone varchar(20) unique,
	is_whatsapp boolean default false,
	reputacao_media decimal(4,2) default 0.0,
	
	constraint pk_usuario primary key (id),
	
	constraint fk_localidade foreign key (id_localidade)
		references localidade (id_localidade)
		on update cascade
		on delete set null
);
	
	
create table material (
	id_material int generated always as identity,
	categoria_id int not null,
	dono_id int not null,
	nome_item varchar(100),
	descricao text,
	estado_conservacao varchar(50),
	quantidade int default 1 check (quantidade > 0), 
	
	constraint pk_material primary key (id_material),
	
	constraint fk_categoria foreign key (categoria_id)
		references categoria (id_categoria)
		on update cascade
		on delete restrict,
		
	constraint fk_us_dono foreign key (dono_id)
		references usuario (id_usuario)
		on update cascade
		on delete cascade
		
	constraint ck_estado check (estado_conservacao in ('Novo', 'Bom', 'Usado'))
);
	
create table foto_material (
	id_foto int generated always as identity,
	id_material int not null,
	url_arquivo varchar(500) not null,
	data_upload timestamp default current_timestamp,
		
	constraint pk_foto primary key (id_foto),
		
	constraint fk_material foreign key (id_material)
		references material (id_material)
		on update cascade
		on delete cascade
);

	create table doacao (
		id_doacao int generated always as identity,
		doador_id int not null,
		receptor_id int not null,
		pontocoleta_id int not null,
		anuncio_id int unique,
		forma_entrega varchar(50),
		status varchar(50) default 'PENDENTE',
		data_confirmacao timestamp,
		
		constraint pk_doacao primary key (id_doacao),
		
		constraint fk_doador foreign key (doador_id)
		references usuario (id_usuario)
		on update cascade
		on delete restrict, 
		
		constraint fk_receptor foreign key (receptor_id)
		references usuario (id_usuario)
		on update cascade
		on delete restrict, 
		
		constraint fk_ponto foreign key (pontocoleta_id)
		references ponto_coleta (id_ponto_coleta)
		on update cascade
		on delete restrict, 
		
		constraint fk_anuncio foreign key (anuncio_id)
		references anuncio (id_anuncio)
		on update cascade
		on delete restrict

		constraint ck_doacao_status CHECK (status IN ('PENDENTE', 'AGENDADO', 'CONCLUIDO', 'CANCELADO')),
    -- Regra de negócio: Doador não pode ser o receptor
    	constraint ck_doador_diferente_receptor CHECK (doador_id <> receptor_id)
);
	
create table categoria (
	id_categoria int generated always as identity,
	nome varchar(100)
	
	constraint pk_categoria primary key (id_categoria)
);
	
create table anuncio (
	id_anuncio int generated always as identity,
	id_usuario int not null,
	id_material int not null,
	titulo varchar(100) not null,
	data_public timestamp default current_timestamp,
	data_expi timestamp,
	status varchar (20) default 'ATIVO',
	
	constraint pk_anuncio primary key (id_anuncio),
	
	constraint fk_usuario foreign key (id_usuario)
	references usuario (id_usuario)
		on update cascade
		on delete cascade,
		
	constraint fk_material foreign key (id_material)
	references material (id_material)
		on update cascade
		on delete cascade
	
	constraint ck_status check (status in ('ATIVO', 'PAUSADO', 'FINALIZADO'))
);
		
		
		
	
	
	
	