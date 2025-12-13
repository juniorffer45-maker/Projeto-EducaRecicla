class Usuario: #Criada por Aldemir Ferreira da Silva Junior
#Representa o Usuario

    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.nasc = nasc
        self.cidade = cidade
        self.estado = estado

    #Criada por Beatriz Benigno de Vasconcelos
    # NOVA PROPRIEDADE: Começa sempre como Falso (Usuário comum)
        self.admin = False 

    def definir_como_administrador(self):
        #Transforma este usuário em um administrador.
        self.admin = True
        print(f"Permissão de ADMIN concedida ao usuário: {self.nome}")

    def criar_Email(self): #Criação de Email
        self.email = input("Digite seu email: ")

    def criar_Senha(self): #Criação de Senha
        while True:
            senha = input("Crie sua senha (mín. 6 caracteres): ")
            if len(senha) >= 6:
                self.senha = senha
                break
            print("Senha muito curta!")                    

    def inserir_Telefone(self): #Inserção de Telefone
        self.telefone = input("Digite seu telefone: ")

    def inserir_Cidade(self): #Inserção de Cidade
        self.cidade = input("Digite sua cidade: ")

    def inserir_Estado(self): #Inserção de Estado
        self.estado = input("Digite seu estado: ")

# CLASSES FILHAS (HERANÇA)

class Receptor(Usuario): #Criada por Maria Ivanilda Irineu de Lima 
    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado, materiaisRecebidos):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiaisRecebidos = materiaisRecebidos
        self.nota = None
        self.descricaoAvaliacao = None

    def definirNota(self, nota):
        #Define a nota dada ao receptor.
        self.nota = nota
        print(f"Nota registrada: {nota}")

    def definirDescricaoAval(self, descricao):
        #Define a descrição da avaliação.
        self.descricaoAvaliacao = descricao
        print(f"Descrição registrada: {descricao}")

    def __str__(self):
        return (
            f"Receptor:\n"
            f"Materiais Recebidos: {self.materiaisRecebidos}\n"
            f"Nota: {self.nota}\n"
            f"Descrição: {self.descricaoAvaliacao}")


class Doador(Usuario): #Criada por Ana Karla Pontes de Souza
    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiais_doados = 0       

    def getNota(self, doacao_referencia): 
        #Busca a nota dada pelo Receptor naquela transação específica.
        print(f"Buscando nota da Doação {doacao_referencia.codigo_doacao}...")
        
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."

        if doacao_referencia.nota is not None:
            return doacao_referencia.nota # Retorna a nota salva
        else:
            return "Nota ainda não registrada pelo receptor."

    def getDescricaoAv(self, doacao_referencia):
        #Busca a Descrição de Avaliação dada pelo Receptor para a transação.
        print(f"Buscando descrição de avaliação da Doação {doacao_referencia.codigo_doacao}...")
        
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."

        if doacao_referencia.desc_av is not None:
            return doacao_referencia.desc_av # Retorna a descrição salva
        else:
            return "Descrição de avaliação ainda não registrada pelo receptor."


    def getCod(self, codigodoacao): # Busca pelo Codigo da Doação
        doacao_id = input("Digite o ID da doação: ")
        return codigodoacao

      

class Material: #Criada por Aldemir Ferreira da Silva Junior
#Representa o item/material que esta sendo doado
    
        def __init__(self, titulo, categoria, descricao, conservacao, localizacao):
            self.titulo = titulo
            self.categoria = categoria
            self.descricao = descricao
            self.conservacao = conservacao
            self.localizacao = localizacao

        def definir_Titulo(self):
            self.titulo = input("Digite o Titulo do Material: ")

        def definir_Categ(self):
            self.categoria = input("Digite a Categoria do Material: ")
        
        def definir_Desc(self):
            self.descricao = input("Descreva o material: ")

        def definir_Cons(self):
            self.conservacao = input("Descreva o Estado de Conservação: ")

        def definir_Loc(self):
            self.localizacao = input("Descreva a Localização de Retirada: ")       



class Doação: #Criada por João Paulo Lima David
    def __init__(self, codigo_doacao, doador, receptor, materiais):

        # Atributos específicos da transação
        self.codigo_doacao = codigo_doacao 
        self.nota = None           # Nota [int]
        self.desc_av = None        # Descrição/Avaliação [string(500)]
        self.categoria_doacao = None  # Categoria da Doação [string]

        # Relacionamentos com outras classes
        self.doador = doador
        self.receptor = receptor 
        self.materiais = materiais # Lista de Materiais doados

        def definir_nota(self, nota: int):
            #Define a nota da transação (método do diagrama).
            self.nota = nota
        
        def desc_ou_just(self, descricao: str):
            #Define a descrição ou justificativa da doação (método do diagrama).
            self.desc_av = descricao
        
        def cat_doacao(self, categoria: str):
            #Define a categoria da doação (método do diagrama).
            self.categoria_doacao = categoria
        
        def adicionar_material(self, material: 'Material'):
            #Método auxiliar para adicionar um material à lista.
            self.materiais.append(material)



