class FilaEspera:
    def __init__(self):
        self.apartamentos = []

    def adicionar(self, apartamento):
        self.apartamentos.append(apartamento)

    def remover(self):
        if self.apartamentos:
            return self.apartamentos.pop(0)
        return None

    def imprimir(self):
        if not self.apartamentos:
            print("Fila de espera está vazia.")
        else:
            print("Fila de espera por vagas de garagem:")
            for apartamento in self.apartamentos:
                print(f"Apartamento {apartamento.numero}")