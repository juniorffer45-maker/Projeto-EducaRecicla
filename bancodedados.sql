-- Tabelas 7 a 12

CREATE TABLE Localidade (
	id_localidade INTEGER PRIMARY KEY,
	nome_cidade VARCHAR(100) UNIQUE KEY,
	sigla_cidade VARCHAR(100) UNIQUE KEY,
)

CREATE TABLE PontoColeta (
	id_ponto_coleta INTEGER PRIMARY KEY,
	id_localidade INTEGER Not Null,
	nome_local VARCHAR(100),
	endereco_completo VARCHAR(100),
	horario_funcionamento VARCHAR(100),
	
	CONSTRAINT fk_id_localidade
		FOREIGN KEY (id_localidade)
		REFERENCES localidade(id_localidade)	
		ON UPDATE CASCADE
		ON DELETE RESTRICT
);


CREATE TABLE Mensagem (
	id_mensagem Integer PRIMARY KEY,
	id_remetente INTEGER,
	id_destinatario INTEGER,
	id_anuncio INTEGER,
	conteudo TEXT,
	data_envio DATE,
	lida_em BOOLEAN DEFAULT FALSE,

	CONSTRAINT fk_id_remetente
		FOREIGN KEY (id_remetente)
		REFERENCES usuario(id_usuario)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
		
	CONSTRAINT fk_id_destinatario
		FOREIGN KEY (id_destinatario)
		REFERENCES usuario(id_usuario)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
		
	CONSTRAINT fk_id_anuncio
		FOREIGN KEY (id_anuncio)
		REFERENCES anuncio(id_anuncio)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
);


CREATE TABLE Notificacao (
	id_notificacao INTEGER PRIMARY KEY,
	id_usuario INTEGER NOT NULL,
	id_origem INTEGER NOT NULL,
	data_criacao DATE NOT NULL,
	titulo VARCHAR(50) NOT NULL,
	mensagem VARCHAR(255) NOT NULL,
	--texto VARCHAR(255), parece ser algo redundante
	lida BOOLEAN DEFAULT FALSE,
	tipo VARCHAR(50),
	
	CONSTRAINT fk_id_usuario
		FOREIGN KEY (id_usuario)
		REFERENCES usuario(id_usuario)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
		
	CONSTRAINT fk_id_origem
    FOREIGN KEY (id_origem)
    REFERENCES anuncio(id_anuncio) 
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE Moderacao (
	id_moderacao INTEGER NOT NULL PRIMARY KEY,
	id_anuncio INTEGER NOT NULL,
	id_usuario_reportante INTEGER NOT NULL,
	id_usuario_denunciado INTEGER NOT NULL,
	motivo VARCHAR(100) NOT NULL,
	status_resolucao VARCHAR NOT NULL,
	data_registro DATE NOT NULL,
	descricao TEXT NOT NULL,
	
	CONSTRAINT fk_id_anuncio
		FOREIGN KEY (id_anuncio)
		REFERENCES anuncio(id_anuncio)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
	
	CONSTRAINT fk_id_usuario_reportante
		FOREIGN KEY (id_usuario_reportante)
		REFERENCES usuario(id_usuario)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
		
	CONSTRAINT fk_id_usuario_denunciado
		FOREIGN KEY (id_usuario_denunciado)
		REFERENCES usuario(id_usuario)
		ON UPDATE CASCADE
		ON DELETE RESTRICT

);

