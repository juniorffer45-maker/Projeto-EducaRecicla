class Usuario:

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

            
            

class ADM(Usuario):

    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)

    def criar_Email(self): #Criação de Email(ADM)
        return super().criar_Email()
    
    def criar_Senha(self): #Criação de Senha(ADM)
        return super().criar_Senha()
    

class Receptor(Usuario):

    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado, materiaisrecebidos):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiaisrecebidos = materiaisrecebidos

    def inserir_Nota(self, doacao_a_avaliar: 'Doacao'):
        """Permite ao receptor dar uma nota para uma doação específica."""
        if doacao_a_avaliar.receptor != self:
             print("Erro: Esta doação não é sua para avaliar.")
             return

        while True:
            try:
                # 1. Obter a nota do usuário
                nota = int(input(f"Avalie a doação {doacao_a_avaliar.codigo_doacao} (1 a 5): "))
                
                # 2. Chamar o método da Doacao para registrar a nota
                if doacao_a_avaliar.definir_nota(nota):
                    break # Sai do loop se a nota for válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    def inserir_Descricao(self, doacao_a_avaliar: 'Doacao'): 
        """Permite ao receptor inserir uma descrição de avaliação para uma doação específica."""
        if doacao_a_avaliar.receptor != self:
             print("Erro: Esta doação não é sua para avaliar.")
             return
             
        descricao = input(f"Insira a descrição de avaliação para {doacao_a_avaliar.codigo_doacao}: ")
        
        # Chama o método da Doacao para registrar a descrição
        doacao_a_avaliar.desc_ou_just(descricao)

class Doador(Usuario):

    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado, materiaisdoados):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiaisdoados = materiaisdoados

    def getNota(self, doacao_referencia: 'Doacao'): 
        #"""Busca a nota dada pelo Receptor naquela transação específica."""
        print(f"Buscando nota da Doação {doacao_referencia.codigo_doacao}...")
        
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."

        if doacao_referencia.nota is not None:
            return doacao_referencia.nota # Retorna a nota salva
        else:
            return "Nota ainda não registrada pelo receptor."

    def getDescricaoAv(self, doacao_referencia: 'Doacao'):
        """Busca a Descrição de Avaliação dada pelo Receptor para a transação."""
        print(f"Buscando descrição de avaliação da Doação {doacao_referencia.codigo_doacao}...")
        
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."

        if doacao_referencia.desc_av is not None:
            return doacao_referencia.desc_av # Retorna a descrição salva
        else:
            return "Descrição de avaliação ainda não registrada pelo receptor."

    def getCod(self): # Busca pelo Codigo da Doação
        doacao_id = input("Digite o ID da doação: ")
        return


class Material:

        def __init__(self, titulo, categoria, descricao, conservacao, localizacao):
            self.titulo = titulo
            self.categoria = categoria
            self.descricao = descricao
            self.conservacao = conservacao
            self.localizacao = localizacao

        def definir_Titulo(self):
            self.titulo = input("Digite o Titulo do Material: ")

        def definir_Cat(self):
            pass
        
        def definir_Desc(self):
            self.descricao = input("Descreva o material: ")

        def definir_Cons(self):
            pass

        def definir_Loc(self):
            pass


#class Doaçao(Material):

#    def __init__(self, titulo, categoria, descricao, conservacao, localizacao, nota, desc_av, codigo_doacao):
#        super().__init__(titulo, categoria, descricao, conservacao, localizacao)
#        self.nota = nota
#        self.desc_av = desc_av
 #       self.codigo_doacao = codigo_doacao

class Doacao:
    
    #Representa a transação de doação.
    #Ela associa um Doador, um Receptor e os Materiais envolvidos.
    
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
        #"""Define a nota da transação, dada pelo receptor."""
        if 1 <= nota <= 5: # Adiciona validação
            self.nota = nota
            print(f"Nota {nota} registrada na doação {self.codigo_doacao}.")
            return True
        else:
            print("Erro: A nota deve ser entre 1 e 5.")
            return False
        
    def desc_ou_just(self, descricao: str):
        """Define a descrição ou justificativa da doação, dada pelo receptor."""
        if len(descricao) > 0:
            self.desc_av = descricao
            print(f"Descrição de avaliação registrada na doação {self.codigo_doacao}.")
            return True
        else:
            print("Erro: A descrição não pode ser vazia.")
            return False
        
    def cat_doacao(self, categoria: str):
        #"""Define a categoria da doação (método do diagrama)."""
        self.categoria_doacao = categoria
        
    def adicionar_material(self, material: 'Material'):
        #"""Método auxiliar para adicionar um material à lista."""
        self.materiais.append(material)








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


    def getCod(self, codigodoacao): # Busca pelo Codigo de alguma doação
        doacao_id = input("Digite o ID da doação: ")
        return codigodoacao

