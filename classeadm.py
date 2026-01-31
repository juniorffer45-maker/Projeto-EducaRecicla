#Criada por Beatriz Benigno de Vasconcelos
    # NOVA PROPRIEDADE: Começa sempre como Falso (Usuário comum)
        self.admin = False 

    def definir_como_administrador(self):
        #Transforma este usuário em um administrador.
        self.admin = True
        print(f"Permissão de ADMIN concedida ao usuário: {self.nome}")
