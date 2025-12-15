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

    ##Aldemir

    def inserir_Nome(self): #Inserção de Nome
        while True:
            novo_nome = input("Digite seu nome completo: ").strip()
            if len(novo_nome) >= 3 and " " in novo_nome:
                self.nome = novo_nome
                print(f"Nome atualizado para: {self.nome}")
                break
            else:
                print("ERRO: Por favor, digite seu nome completo (mínimo de 3 caracteres e sobrenome).")

    def inserir_Nasc(self): #Inserção de Data de Nascimento
        #Solicita e atualiza a data de nascimento, com validação de formato (DD/MM/AAAA)
        while True:
            data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
            if len(data_nasc) == 10 and data_nasc[2] == '/' and data_nasc[5] == '/':
                self.nasc = data_nasc
                print(f"Data de nascimento atualizada para: {self.nasc}")
                break
            else:
                print("ERRO: O formato da data está incorreto. Use o padrão DD/MM/AAAA (ex: 31/12/1990).")

    
    def criar_Email(self): #Criação de Email
        while True:
            email = input("Digite seu email: ").strip()
            #Checa se o email contém '@' e '.'
            if "@" not in email or "." not in email:
                print("ERRO: O e-mail deve conter o símbolo '@' e o símbolo '.' (ponto).")
                continue # Volta ao início do loop
            #Checa se o '@' está antes do '.'
            # Verificação de estrutura (ex: a@b.com é válido, a.b@com não é)
            indice_arroba = email.find("@")
            indice_ponto = email.rfind(".") 
            #Verifica se o arroba está no meio e se o ponto vem depois
            if indice_arroba > 0 and indice_ponto > indice_arroba and indice_ponto < len(email) - 1:
                self.email = email
                print(f"E-mail '{email}' registrado com sucesso.")
                break
            else:
                print("ERRO: O formato do e-mail está incorreto (verifique a posição de '@' e '.').")

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
        super()._init_(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiais_doados = 0       
    
    def getNota(self, doacao_referencia): #Buscará as notas dadas pelo Usuario Receptor e irá calcular sua média, sendo esta a Nota Definitiva do Usuario Doador.
        print(f"Buscando nota da Doação {doacao_referencia.codigo_doacao}...")
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."
        if doacao_referencia.nota is not None:
            return doacao_referencia.nota # Retorna a nota salva
        else:
            return "Nota ainda não registrada pelo receptor."

    def getDescricaoAv(self, doacao_referencia): #Buscará o comentario da Avaliação dada pelo Usuario Receptor em relação a transação.      
        print(f"Buscando descrição de avaliação da Doação {doacao_referencia.codigo_doacao}...")
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."
        if doacao_referencia.desc_av is not None:
            return doacao_referencia.desc_av # Retorna a descrição salva
        else:
            return "Descrição de avaliação ainda não registrada pelo receptor."

    def getCod(self, codigodoacao): # Buscará pelo codigo de alguma doação e irá disponibilizar suas informações.
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

        def definir_Titulo(self): #Define o titulo do Material
            self.titulo = input("Digite o Titulo do Material: ")

        def definir_Categ(self): #Define a Categoria do Material
            self.categoria = input("Digite a Categoria do Material: ")
        
        def definir_Desc(self): #Inserção da Descrição do Material
            self.descricao = input("Descreva o material: ")

        def definir_Cons(self): #Inserção do Estado de Conservação do Material
            self.conservacao = input("Descreva o Estado de Conservação: ")

        def definir_Loc(self): #Definição do Local de Retirada do Material
            self.localizacao = input("Descreva a Localização de Retirada: ")       


class Doação: #Criada por João Paulo Lima David
    def __init__(self, codigo_doacao, doador, receptor, materiais):

        # Atributos específicos da transação
        self.codigo_doacao = codigo_doacao 
        self.nota = None          
        self.desc_av = None       
        self.categoria_doacao = None  

        # Relacionamentos com outras classes
        self.doador = doador
        self.receptor = receptor 
        self.materiais = materiais # Lista de Materiais doados

        def definir_nota(self, nota: int): #Define a nota da transação 
            self.nota = nota
        
        def desc_ou_just(self, descricao: str): #Define a descrição da doação 
            self.desc_av = descricao
        
        def cat_doacao(self, categoria: str): #Define a categoria da doação
            self.categoria_doacao = categoria
        
        def adicionar_material(self, material: 'Material'): #Método auxiliar para adicionar um material à lista.
            self.materiais.append(material)










