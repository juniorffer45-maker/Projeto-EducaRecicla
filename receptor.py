class Receptor:
    def _init_(self, materiaisRecebidos: int):
        self.materiaisRecebidos = materiaisRecebidos
        self.nota = None
        self.descricaoAvaliacao = None

    def definirNota(self, nota):
        """Define a nota dada ao receptor."""
        self.nota = nota
        print(f"Nota registrada: {nota}")

    def definirDescricaoAval(self, descricao):
        """Define a descrição da avaliação."""
        self.descricaoAvaliacao = descricao
        print(f"Descrição registrada: {descricao}")

    def _str_(self):
        return (
            f"Receptor:\n"
            f"Materiais Recebidos: {self.materiaisRecebidos}\n"
            f"Nota: {self.nota}\n"
            f"Descrição: {self.descricaoAvaliacao}")
