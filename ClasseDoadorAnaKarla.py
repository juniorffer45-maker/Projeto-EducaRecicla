#Ana Karla
class Doador(Usuario):
    def _init_(self, nome, email, senha, telefone, nasc, cidade, estado):
        # Aqui o Doador "nasce" já chamando a construção do Usuario (super)
        super()._init_(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiais_doados = 0       
    
    def getNota(self, nota):
        return nota

    def getDescricaoAv(self, desc_av):       

    def getCod(self, codigodoacao):
        return codigodoacao
