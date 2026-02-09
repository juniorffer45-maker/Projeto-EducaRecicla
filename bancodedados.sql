CREATE TABLE Localidade (
    id_localidade INTEGER PRIMARY KEY,
    nome_cidade VARCHAR(100) UNIQUE,
    sigla_cidade VARCHAR(100) UNIQUE
);

CREATE TABLE categoria (
    id_categoria int generated always as identity,
    nome varchar(100),
    constraint pk_categoria primary key (id_categoria)
);


CREATE TABLE usuario (
    id_usuario int generated always as identity, 
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
    
    constraint pk_usuario primary key (id_usuario),
    constraint fk_localidade foreign key (id_localidade)
        references localidade (id_localidade)
        on update cascade
        on delete set null
);


CREATE TABLE material (
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
        on delete cascade,
    constraint ck_estado check (estado_conservacao in ('Novo', 'Bom', 'Usado'))
);

CREATE TABLE anuncio (
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
        on delete cascade,
    constraint ck_status check (status in ('ATIVO', 'PAUSADO', 'FINALIZADO'))
);


CREATE TABLE foto_material (
    id_foto int generated always as identity,
    id_material int not null,
    url_arquivo varchar(500) not null,
    data_upload timestamp default current_timestamp,
    constraint pk_foto primary key (id_foto),
    constraint fk_material_foto foreign key (id_material)
        references material (id_material)
        on update cascade
        on delete cascade
);

CREATE TABLE PontoColeta (
    id_ponto_coleta INTEGER PRIMARY KEY,
    id_localidade INTEGER Not Null,
    nome_local VARCHAR(100),
    endereco_completo VARCHAR(100),
    horario_funcionamento VARCHAR(100),
    CONSTRAINT fk_id_localidade_ponto
        FOREIGN KEY (id_localidade)
        REFERENCES localidade(id_localidade)    
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE doacao (
    id_doacao int generated always as identity,
    doador_id int not null,
    receptor_id int not null,
    pontocoleta_id int not null,
    anuncio_id int unique,
    forma_entrega varchar(50),
    status varchar(50) default 'PENDENTE',
    data_confirmacao timestamp,
    
    constraint pk_doacao primary key (id_doacao),
    constraint fk_doador foreign key (doador_id) references usuario (id_usuario),
    constraint fk_receptor foreign key (receptor_id) references usuario (id_usuario),
    constraint fk_ponto foreign key (pontocoleta_id) references PontoColeta (id_ponto_coleta),
    constraint fk_anuncio foreign key (anuncio_id) references anuncio (id_anuncio),
    constraint ck_doacao_status CHECK (status IN ('PENDENTE', 'AGENDADO', 'CONCLUIDO', 'CANCELADO')),
    constraint ck_doador_diferente_receptor CHECK (doador_id <> receptor_id)
);

CREATE TABLE Mensagem (
    id_mensagem Integer PRIMARY KEY,
    id_remetente INTEGER,
    id_destinatario INTEGER,
    id_anuncio INTEGER,
    conteudo TEXT,
    data_envio timestamp default current_timestamp,
    lida BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_id_remetente FOREIGN KEY (id_remetente) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_destinatario FOREIGN KEY (id_destinatario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_anuncio_msg FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio)
);

CREATE TABLE Notificacao (
    id_notificacao INTEGER PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    id_origem INTEGER NOT NULL,
    data_criacao timestamp default current_timestamp,
    titulo VARCHAR(50) NOT NULL,
    mensagem VARCHAR(255) NOT NULL,
    lida BOOLEAN DEFAULT FALSE,
    tipo VARCHAR(50),
    
    CONSTRAINT fk_notif_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_notif_anuncio FOREIGN KEY (id_origem) REFERENCES anuncio(id_anuncio)
);

CREATE TABLE Moderacao (
    id_moderacao INTEGER NOT NULL PRIMARY KEY,
    id_anuncio INTEGER NOT NULL,
    id_usuario_reportante INTEGER NOT NULL,
    id_usuario_denunciado INTEGER NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    status_resolucao VARCHAR(50) NOT NULL,
    data_registro timestamp default current_timestamp,
    descricao TEXT NOT NULL,
    
    CONSTRAINT fk_mod_anuncio FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio),
    CONSTRAINT fk_mod_reportante FOREIGN KEY (id_usuario_reportante) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_mod_denunciado FOREIGN KEY (id_usuario_denunciado) REFERENCES usuario(id_usuario)
);


