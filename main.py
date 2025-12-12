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

class Admin(Usuario): #Criada por Beatriz Benigno de Vasconcelos
    #Estou passando os parametros opcionais para ele não pedir os dados de cara. Porque se pedir e não tiver, dá erro.
    def __init__(self, nome, email="", senha="", telefone, nasc):
        super().__init__(nome, email, senha, telefone, nasc)
        self.email = email
        self.senha = senha

    def definir_email(self, email): #Criação de Email(ADM)
        self.email = email
        return super().criar_Email()
        
    def definir_senha(self, senha): #Criação de Senha(ADM)
        self.senha = senha
        return super().criar_Senha()


class Doador(Usuario): #Criada por Ana Karla Pontes de Souza
    def _init_(self, nome, email, senha, telefone, nasc, cidade, estado):
        # Aqui o Doador "nasce" já chamando a construção do Usuario (super)
        super()._init_(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiais_doados = 0       
    
    def getNota(self, nota): #Busca pela Nota dada pelo Avaliador
        print("Buscando nota do doador...")
        return nota

    def getDescricaoAv(self, desc_av): #Busca pela Descrição do Avaliador
        print("Buscando descrição de avaliação...")
        return desc_av

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

        def definir_Cat(self):
            self.categoria = input("Digite a Categoria do Material: ")
        
        def definir_Desc(self):
            self.descricao = input("Descreva o material: ")

        def definir_Cons(self):
            self.conservacao = input("Descreva o Estado de Conservação: ")

        def definir_Loc(self):
            self.localizacao = input("Descreva a Localização de Retirada: ")       



class Doação: #Criada por João Paulo Lima David
    def __init__(self, codigo_doacao: str, doador, receptor, materiais):

        # Atributos específicos da transação
        self.codigo_doacao = codigo_doacao 
        self.nota = None           # Nota [int]
        self.desc_av = None        # Descrição/Avaliação [string(500)]
        self.categoria_doacao = None # Categoria da Doação [string]

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

