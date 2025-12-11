
    Representa a transação de doação.
    Ela associa um Doador, um Receptor e os Materiais envolvidos.
    """ Classe doação:
    def __init__(self, codigo_doacao: str, doador, receptor, materiais):

        # Atributos específicos da transação
        self.codigo_doacao = codigo_doacao 
        self.nota = None           # Nota [int]
        self.desc_av = None        # Descrição/Avaliação [string(500)]
        self.categoria_doacao = None # Categoria da Doação [string]