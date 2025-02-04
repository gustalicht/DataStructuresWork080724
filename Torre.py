class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.apartamentos = []

    def adicionar_apartamento(self, apartamento):
        self.apartamentos.append(apartamento)

    def id_existe(self, id):
        for apartamento in self.apartamentos:
            if apartamento.id == id:
                return True
        return False

    def numero_existe(self, numero):
        for apartamento in self.apartamentos:
            if apartamento.numero == numero:
                return True
        return False
    def quantidade_apartamentos(self):
        return len(self.apartamentos)

    def cadastrar(self):
        print(f"Torre {self.nome} cadastrada com endereço {self.endereco}")

    def imprimir(self):
        print(f"Torre {self.nome}, Endereço: {self.endereco}")
