class Usuario:
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

class Admin(Usuario):
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
        

class Material:
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



