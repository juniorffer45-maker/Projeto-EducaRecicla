CREATE TABLE localidade (
    id_localidade INT GENERATED ALWAYS AS IDENTITY,
    nome_cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) not null,
    UNIQUE (nome_cidade, uf),
    
    constraint pk_localidade primary key (id_localidade)
);

CREATE TABLE categoria (
    id_categoria INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(100) not null unique,
    
    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE usuario (
    id_usuario INT GENERATED ALWAYS AS IDENTITY,
    id_localidade INT,
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
    id_material INT GENERATED ALWAYS AS IDENTITY,
    categoria_id INT NOT NULL,
    dono_id INT NOT NULL,
    nome_item VARCHAR(100) not null,
    descricao TEXT,
    estado_conservacao VARCHAR(50),
    quantidade INT DEFAULT 1 CHECK (quantidade > 0), 
    
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
    id_anuncio INT GENERATED ALWAYS AS IDENTITY,
    id_material INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    data_public TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_expi TIMESTAMP,
    status VARCHAR (20) DEFAULT 'ATIVO',
    
    CONSTRAINT pk_anuncio PRIMARY KEY (id_anuncio),
        
    CONSTRAINT fk_material FOREIGN KEY (id_material)
        REFERENCES material (id_material)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
        
    CONSTRAINT ck_status CHECK (status IN ('ATIVO', 'PAUSADO', 'FINALIZADO'))
);

CREATE TABLE foto_material (
    id_foto INT GENERATED ALWAYS AS IDENTITY,
    id_material INT NOT NULL,
    url_arquivo VARCHAR(500) NOT NULL,
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_foto PRIMARY KEY (id_foto),
    CONSTRAINT fk_material_foto FOREIGN KEY (id_material)
        REFERENCES material (id_material)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE pontocoleta (
    id_ponto_coleta INT GENERATED ALWAYS AS IDENTITY,
    id_localidade INT NOT NULL,
    nome_local VARCHAR(100) not null,
    endereco_completo VARCHAR(255),
    horario_funcionamento VARCHAR(100),
    
    CONSTRAINT pk_ponto_coleta PRIMARY KEY (id_ponto_coleta),
    
    CONSTRAINT fk_localidade_ponto FOREIGN KEY (id_localidade)
        REFERENCES localidade(id_localidade)   
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE doacao (
    id_doacao INT GENERATED ALWAYS AS IDENTITY,
    doador_id INT NOT NULL,
    receptor_id INT NOT NULL,
    pontocoleta_id INT NOT NULL,
    anuncio_id INT UNIQUE,
    forma_entrega VARCHAR(50),
    status VARCHAR(50) DEFAULT 'PENDENTE',
    data_confirmacao TIMESTAMP,
    
    CONSTRAINT pk_doacao PRIMARY KEY (id_doacao),
    
    CONSTRAINT fk_doador FOREIGN KEY (doador_id) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_receptor FOREIGN KEY (receptor_id) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_ponto FOREIGN KEY (pontocoleta_id) REFERENCES pontocoleta (id_ponto_coleta),
    CONSTRAINT fk_anuncio FOREIGN KEY (anuncio_id) REFERENCES anuncio (id_anuncio),
    CONSTRAINT ck_doacao_status CHECK (status IN ('PENDENTE', 'AGENDADO', 'CONCLUIDO', 'CANCELADO')),
    CONSTRAINT ck_doador_diferente_receptor CHECK (doador_id <> receptor_id)
);

CREATE TABLE mensagem (
    id_mensagem INT GENERATED ALWAYS AS IDENTITY,
    id_remetente INT not null,
    id_destinatario INT not null,
    id_anuncio INT,
    conteudo TEXT not null,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_leitura TIMESTAMP,

    CONSTRAINT pk_mensagem PRIMARY KEY (id_mensagem),
    
    CONSTRAINT fk_id_remetente FOREIGN KEY (id_remetente) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_destinatario FOREIGN KEY (id_destinatario) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_id_anuncio_msg FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio)
);

CREATE TABLE notificacao (
    id_notificacao INT GENERATED ALWAYS AS IDENTITY,
    id_usuario INT NOT NULL,
   
    id_anuncio INT,
    id_mensagem INT,
    id_doacao INT,
    
    titulo VARCHAR(50) NOT NULL,
    mensagem VARCHAR(255) NOT NULL,
    lida BOOLEAN DEFAULT FALSE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT pk_notificacao PRIMARY KEY (id_notificacao),
    
    CONSTRAINT fk_notif_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    CONSTRAINT fk_notif_anuncio FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio) ON DELETE CASCADE,
    CONSTRAINT fk_notif_mensagem FOREIGN KEY (id_mensagem) REFERENCES mensagem(id_mensagem) ON DELETE CASCADE,
    CONSTRAINT fk_notif_doacao FOREIGN KEY (id_doacao) REFERENCES doacao(id_doacao) ON DELETE CASCADE,
    
    CONSTRAINT ck_uma_origem CHECK (
        (id_anuncio IS NOT NULL AND id_mensagem IS NULL AND id_doacao IS NULL) OR
        (id_anuncio IS NULL AND id_mensagem IS NOT NULL AND id_doacao IS NULL) OR
        (id_anuncio IS NULL AND id_mensagem IS NULL AND id_doacao IS NOT NULL) OR
        (id_anuncio IS NULL AND id_mensagem IS NULL AND id_doacao IS NULL)
));

CREATE TABLE moderacao (
    id_moderacao INT GENERATED ALWAYS AS IDENTITY,
    id_anuncio INT NOT NULL,
    id_reportante INT NOT NULL,
    id_denunciado INT NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    status_resolucao VARCHAR(50) not null default 'ABERTO',
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT NOT NULL,
    
    CONSTRAINT pk_moderacao PRIMARY KEY (id_moderacao),
    
    CONSTRAINT fk_mod_anuncio FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio),
    CONSTRAINT fk_mod_reportante FOREIGN KEY (id_reportante) REFERENCES usuario(id_usuario),
    CONSTRAINT fk_mod_denunciado FOREIGN KEY (id_denunciado) REFERENCES usuario(id_usuario),
    CONSTRAINT ck_mod_status CHECK (status_resolucao IN ('ABERTO', 'EM_ANALISE', 'RESOLVIDO', 'REJEITADO'))
);

-- --- ÍNDICES DE PERFORMANCE

-- Acelera: "Ver materiais do usuário X"
CREATE INDEX idx_material_dono ON material(dono_id);

-- Acelera: "Ver materiais de uma categoria"
CREATE INDEX idx_material_categoria ON material(categoria_id);

-- Acelera: "Ver fotos de um material"
CREATE INDEX idx_foto_material ON foto_material(id_material);

-- Acelera: "Ver histórico de doações (como doador e receptor)"
CREATE INDEX idx_doacao_doador ON doacao(doador_id);
CREATE INDEX idx_doacao_receptor ON doacao(receptor_id);

-- Acelera: "Ver chat entre duas pessoas"
CREATE INDEX idx_mensagem_participantes ON mensagem(id_remetente, id_destinatario);

-- Acelera: "Ver minhas notificações não lidas"
CREATE INDEX idx_notificacao_usuario ON notificacao(id_usuario) WHERE lida = FALSE;


