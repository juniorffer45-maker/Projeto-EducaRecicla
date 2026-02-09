CREATE TABLE Localidade (
    id_localidade INTEGER GENERATED ALWAYS AS IDENTITY,
    nome_cidade VARCHAR(100) UNIQUE NOT NULL,
    sigla_cidade VARCHAR(100) UNIQUE NOT NULL,
    uf VARCHAR(2) UNIQUE (nome_cidade, uf)
    CONSTRAINT pk_localidade PRIMARY KEY (id_localidade)
);

CREATE TABLE categoria (
    id_categoria INTEGER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(100) NOT NULL,
    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE usuario (
    id_usuario INTEGER GENERATED ALWAYS AS IDENTITY,
    id_localidade INTEGER,
    nome_completo VARCHAR(100) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    biografia TEXT,
    foto_perfil_url VARCHAR(500),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    telefone VARCHAR(20) UNIQUE,
    is_whatsapp BOOLEAN DEFAULT FALSE,
    reputacao_media DECIMAL(4,2) DEFAULT 0.0,
    
    CONSTRAINT pk_usuario PRIMARY KEY (id_usuario),
    CONSTRAINT fk_localidade FOREIGN KEY (id_localidade)
        REFERENCES localidade (id_localidade)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE material (
    id_material INTEGER GENERATED ALWAYS AS IDENTITY,
    categoria_id INTEGER NOT NULL,
    dono_id INTEGER NOT NULL,
    nome_item VARCHAR(100),
    descricao TEXT,
    estado_conservacao VARCHAR(50),
    quantidade INTEGER DEFAULT 1 CHECK (quantidade > 0), 
    
    CONSTRAINT pk_material PRIMARY KEY (id_material),
    CONSTRAINT fk_categoria FOREIGN KEY (categoria_id)
        REFERENCES categoria (id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_us_dono FOREIGN KEY (dono_id)
        REFERENCES usuario (id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT ck_estado CHECK (estado_conservacao IN ('Novo', 'Bom', 'Usado'))
);

CREATE TABLE anuncio (
    id_anuncio INTEGER GENERATED ALWAYS AS IDENTITY,
    id_usuario INTEGER NOT NULL,
    id_material INTEGER NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    data_public TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_expi TIMESTAMP,
    status VARCHAR (20) DEFAULT 'ATIVO',
    
    CONSTRAINT pk_anuncio PRIMARY KEY (id_anuncio),
    CONSTRAINT fk_usuario FOREIGN KEY (id_usuario)
        REFERENCES usuario (id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_material FOREIGN KEY (id_material)
        REFERENCES material (id_material)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT ck_status CHECK (status IN ('ATIVO', 'PAUSADO', 'FINALIZADO'))
);

CREATE TABLE foto_material (
    id_foto INTEGER GENERATED ALWAYS AS IDENTITY,
    id_material INTEGER NOT NULL,
    url_arquivo VARCHAR(500) NOT NULL,
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_foto PRIMARY KEY (id_foto),
    CONSTRAINT fk_material_foto FOREIGN KEY (id_material)
        REFERENCES material (id_material)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE PontoColeta (
    id_ponto_coleta INTEGER GENERATED ALWAYS AS IDENTITY,
    id_localidade INTEGER NOT NULL,
    nome_local VARCHAR(100),
    endereco_completo VARCHAR(100),
    horario_funcionamento VARCHAR(100),
    CONSTRAINT pk_ponto_coleta PRIMARY KEY (id_ponto_coleta),
    CONSTRAINT fk_id_localidade_ponto
        FOREIGN KEY (id_localidade)
        REFERENCES localidade(id_localidade)   
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE doacao (
    id_doacao INTEGER GENERATED ALWAYS AS IDENTITY,
    doador_id INTEGER NOT NULL,
    receptor_id INTEGER NOT NULL,
    pontocoleta_id INTEGER NOT NULL,
    anuncio_id INTEGER UNIQUE,
    forma_entrega VARCHAR(50),
    status VARCHAR(50) DEFAULT 'PENDENTE',
    data_confirmacao TIMESTAMP,
    
    CONSTRAINT pk_doacao PRIMARY KEY (id_doacao),
    CONSTRAINT fk_doador FOREIGN KEY (doador_id) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_receptor FOREIGN KEY (receptor_id) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_ponto FOREIGN KEY (pontocoleta_id) REFERENCES PontoColeta (id_ponto_coleta),
    CONSTRAINT fk_anuncio FOREIGN KEY (anuncio_id) REFERENCES anuncio (id_anuncio),
    CONSTRAINT ck_doacao_status CHECK (status IN ('PENDENTE', 'AGENDADO', 'CONCLUIDO', 'CANCELADO')),
    CONSTRAINT ck_doador_diferente_receptor CHECK (doador_id <> receptor_id)
);

CREATE TABLE Mensagem (
    id_mensagem INTEGER GENERATED ALWAYS AS IDENTITY,
    id_remetente INTEGER,
    id_destinatario INTEGER,
    id_anuncio INTEGER,
    conteudo TEXT,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lida BOOLEAN DEFAULT FALSE,

    CONSTRAINT pk_mensagem PRIMARY KEY (id_mensagem),
    CONSTRAINT fk_id_remetente FOREIGN KEY (id_remetente) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_destinatario FOREIGN KEY (id_destinatario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_anuncio_msg FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio)
);

CREATE TABLE Notificacao (
    id_notificacao INTEGER GENERATED ALWAYS AS IDENTITY,
    id_usuario INTEGER NOT NULL,
    id_origem INTEGER NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    titulo VARCHAR(50) NOT NULL,
    mensagem VARCHAR(255) NOT NULL,
    lida BOOLEAN DEFAULT FALSE,
    tipo VARCHAR(50),
    
    CONSTRAINT pk_notificacao PRIMARY KEY (id_notificacao),
    CONSTRAINT fk_notif_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_notif_anuncio FOREIGN KEY (id_origem) REFERENCES anuncio(id_anuncio)
);

CREATE TABLE Moderacao (
    id_moderacao INTEGER GENERATED ALWAYS AS IDENTITY,
    id_anuncio INTEGER NOT NULL,
    id_usuario_reportante INTEGER NOT NULL,
    id_usuario_denunciado INTEGER NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    status_resolucao VARCHAR(50) NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT NOT NULL,
    
    CONSTRAINT pk_moderacao PRIMARY KEY (id_moderacao),
    CONSTRAINT fk_mod_anuncio FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio),
    CONSTRAINT fk_mod_reportante FOREIGN KEY (id_usuario_reportante) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_mod_denunciado FOREIGN KEY (id_usuario_denunciado) REFERENCES usuario(id_usuario)
);
