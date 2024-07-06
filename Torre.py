class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.apartamentos = []

    def imprimir(self):
        print(f"Torre {self.nome} - Endereço: {self.endereco}")

    def adicionar_apartamento(self, apartamento):
        self.apartamentos.append(apartamento)

    def apartamento_existe(self, id, numero):
        for ap in self.apartamentos:
            if ap.id == id or ap.numero == numero:
                return True
        return False

    def quantidade_apartamentos(self):
        return len(self.apartamentos)