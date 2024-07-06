class Apartamento:
    def __init__(self, id, numero, vaga=None, torre=None, proximo=None):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
        self.proximo = proximo

    def cadastrar(self, novo_apartamento):
        if self.proximo is None:
            self.proximo = novo_apartamento
        else:
            self.proximo.cadastrar(novo_apartamento)

    def imprimir(self):
        print(f"Apartamento {self.numero} - Torre: {self.torre.nome if self.torre else 'Sem torre associada'} - Vaga: {self.vaga}")