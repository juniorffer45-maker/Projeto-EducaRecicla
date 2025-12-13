from typing import List, Optional, TYPE_CHECKING
import math

#SIMULAÇÃO DE BANCO DE DADOS
# Lista global para simular o armazenamento de todas as instâncias de Doacao.
REPOSITORIO_DOACOES: List['Doacao'] = []

# --- IMPORTAÇÕES PARA TYPE HINTING (Ajudam a Python a entender as referências cruzadas) ---
if TYPE_CHECKING:
    class Doacao: pass
    class Material: pass
    class Receptor: pass
    class Doador: pass

# =========================================================================
# 1. CLASSES DE BASE E USUÁRIOS
# =========================================================================

class Usuario: # Criada por Aldemir Ferreira da Silva Junior
    #Classe base para todos os usuários do sistema

    def __init__(self, nome: str, email: str, senha: str, telefone: str, nasc: str, cidade: str, estado: str):
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

    def inserir_Nome(self):
        #Solicita e atualiza o nome completo do usuário
        while True:
            novo_nome = input("Digite seu nome completo: ").strip()
            if len(novo_nome) >= 3 and " " in novo_nome:
                self.nome = novo_nome
                print(f"Nome atualizado para: {self.nome}")
                break
            else:
                print("ERRO: Por favor, digite seu nome completo (mínimo de 3 caracteres e sobrenome).")

    def inserir_Nasc(self):
        #Solicita e atualiza a data de nascimento, com validação de formato (DD/MM/AAAA)
        while True:
            data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
            
            # Validação básica de formato e comprimento
            if len(data_nasc) == 10 and data_nasc[2] == '/' and data_nasc[5] == '/':
                self.nasc = data_nasc
                print(f"✅ Data de nascimento atualizada para: {self.nasc}")
                break
            else:
                print("ERRO: O formato da data está incorreto. Use o padrão DD/MM/AAAA (ex: 31/12/1990).")



    def criar_Email(self): # Criação de Email
        while True:
            email = input("Digite seu email: ").strip()
            
            #Checa se o email contém '@' e '.'
            if "@" not in email or "." not in email:
                print("ERRO: O e-mail deve conter o símbolo '@' e o símbolo '.' (ponto).")
                continue # Volta ao início do loop
            
            #Checa se o '@' está antes do '.'
            # Isso é uma verificação básica de estrutura (ex: a@b.com é válido, a.b@com não é)
            indice_arroba = email.find("@")
            indice_ponto = email.rfind(".") # rfind pega a última ocorrência

            #Verifica se o arroba está no meio e se o ponto vem depois
            if indice_arroba > 0 and indice_ponto > indice_arroba and indice_ponto < len(email) - 1:
                self.email = email
                print(f"E-mail '{email}' registrado com sucesso.")
                break
            else:
                print("ERRO: O formato do e-mail está incorreto (verifique a posição de '@' e '.').")

    def criar_Senha(self): # Criação de Senha
        while True:
            senha = input("Crie sua senha (mín. 6 caracteres): ")
            if len(senha) >= 6:
                self.senha = senha
                print("Senha criada com sucesso!")
                break
            print("Senha muito curta!")

    def inserir_Telefone(self): # Inserção de Telefone
        self.telefone = input("Digite seu telefone: ")

    def inserir_Cidade(self): # Inserção de Cidade
        self.cidade = input("Digite sua cidade: ")

    def inserir_Estado(self): # Inserção de Estado
        self.estado = input("Digite seu estado: ")


class Doador(Usuario): # Criada por Ana Karla Pontes de Souza 
    #Gerencia doações realizadas, nota individual e nota média geral
    
    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        # Lista de referências a objetos Doacao que este Doador realizou
        self.doacoes_realizadas: List['Doacao'] = []
        self.materiais_doados = 0 
        
    # Metodos de Calculos e Demonstração de Notas
    
    def calcular_media_notas(self) -> float: #Pega as notas recebidas e calcula sua média, sendo esta a Nota Definitiva do Doador
        notas_validas = [d.nota for d in self.doacoes_realizadas if isinstance(d.nota, int) and d.nota > 0]
        
        if not notas_validas:
            return 0.0
        
        media = sum(notas_validas) / len(notas_validas)
        return round(media, 2)

    def getNotaGeral(self) -> str: #Retorna a nota média geral do Doador
        media = self.calcular_media_notas()
        
        if media == 0.0 and not self.doacoes_realizadas:
            return "Nenhuma doação concluída para avaliação."
        
        return f"Média Geral: {media}"
        
    # Metodos de Busca de Doações e suas Notas
    
    def getNota(self, doacao_referencia: 'Doacao'):
        #Busca a nota individual da doação
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."
        return doacao_referencia.nota if doacao_referencia.nota is not None else "Não avaliado"

    def getDescricaoAv(self, doacao_referencia: 'Doacao'):
        #Busca a descrição da doação
        if doacao_referencia.doador != self:
            return "Erro: O doador desta transação não é este usuário."
        return doacao_referencia.desc_av if doacao_referencia.desc_av is not None else "Sem descrição"

    def getCod(self): # Método central de busca
        #Busca uma Doação pelo código, verifica, autoria e exibe nota/descrição
        doacao_id = input("Digite o Código da Doação que você deseja consultar: ")
        
        # Procura no repositório
        doacao_encontrada = next((d for d in REPOSITORIO_DOACOES if d.codigo_doacao == doacao_id), None)

        if doacao_encontrada is None:
            print(f"\n❌ ERRO: Doação com código '{doacao_id}' não encontrada no sistema.")
            return

        if doacao_encontrada.doador != self:
            print(f"\n⚠️ ACESSO NEGADO: Você não é o Doador da transação '{doacao_id}'.")
            return

        print(f"\n--- DETALHES DA DOACAO {doacao_id} ---")
        print(f"Nota Recebida (Específica): {self.getNota(doacao_encontrada)}")
        print(f"Descrição do Receptor: {self.getDescricaoAv(doacao_encontrada)}")
        print("-----------------------------------")
        return doacao_encontrada


class Receptor(Usuario): #Criada por Maria Ivanilda Irineu de Lima
    #Classe que herda de Usuario, representando um receptor de doações
    
    
    def __init__(self, nome, email, senha, telefone, nasc, cidade, estado, materiaisrecebidos: List['Material'] = None):
        super().__init__(nome, email, senha, telefone, nasc, cidade, estado)
        self.materiaisrecebidos = materiaisrecebidos if materiaisrecebidos is not None else []

    # Metodos de Avaliação
    def inserir_Nota(self, doacao_a_avaliar: 'Doacao'):
        #Permite ao receptor dar uma nota (1-5) para uma doação específica
        if doacao_a_avaliar.receptor != self:
             print("Erro: Esta doação não é sua para avaliar.")
             return

        while True:
            try:
                nota = int(input(f"Avalie a doação {doacao_a_avaliar.codigo_doacao} (1 a 5): "))
                if doacao_a_avaliar.definir_nota(nota):
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    def inserir_Descricao(self, doacao_a_avaliar: 'Doacao'):
        #Permite ao receptor inserir uma descrição de avaliação para uma doação específica
        if doacao_a_avaliar.receptor != self:
             print("Erro: Esta doação não é sua para avaliar.")
             return

        descricao = input(f"Insira a descrição de avaliação para {doacao_a_avaliar.codigo_doacao}: ")
        doacao_a_avaliar.desc_ou_just(descricao)


# =========================================================================
# 2. CLASSES DE MATERIAL E TRANSAÇÃO (DOAÇÃO)
# =========================================================================

class Material: # Criada por Aldemir Ferreira da Silva Junior
    #Representa o item/material que está sendo doado
    
    def __init__(self, titulo: str, categoria: str, descricao: str, conservacao: str, localizacao: str):
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


class Doacao: # Criada por João Paulo Lima David
    #Representa a transação de doação (Associações com Doador, Receptor e Material)

    def __init__(self, codigo_doacao: str, doador: 'Doador', receptor: Optional['Receptor'] = None, materiais: List['Material'] = None):

        self.codigo_doacao = codigo_doacao
        self.nota: Optional[int] = None
        self.desc_av: Optional[str] = None
        self.categoria_doacao: Optional[str] = None

        self.doador = doador
        self.receptor = receptor
        self.materiais = materiais if materiais is not None else []

        #Ações de inicialização (Registra a doação no sistema)
        REPOSITORIO_DOACOES.append(self)
        self.doador.doacoes_realizadas.append(self)


    def definir_nota(self, nota: int) -> bool:
        #Registra a nota (1-5) dada pelo receptor
        if 1 <= nota <= 5:
            self.nota = nota
            print(f"Nota {nota} registrada na doação {self.codigo_doacao}.")
            return True
        else:
            print("Erro: A nota deve ser entre 1 e 5.")
            return False
            
    def desc_ou_just(self, descricao: str) -> bool:
        #Registra a descrição/justificativa dada pelo receptor
        if len(descricao) > 0:
            self.desc_av = descricao
            print(f"Descrição de avaliação registrada na doação {self.codigo_doacao}.")
            return True
        return False
        
    def cat_doacao(self, categoria: str):
        #Define a categoria da doação
        self.categoria_doacao = categoria
        
    def adicionar_material(self, material: 'Material'):
        #Adiciona um material à lista da doação
        self.materiais.append(material)


