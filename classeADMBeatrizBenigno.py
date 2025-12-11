class Admin:
    #Estou passando os parametros opcionais para ele não pedir os dados de cara. Porque se pedir e não tiver, dá erro.
    def __init__(self, email="", senha=""):
        self.email = email
        self.senha = senha

    def definir_email(self, email):
        self.email = email

    def definir_senha(self, senha):
        self.senha = senha

    
