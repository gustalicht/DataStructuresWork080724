class ListaApartamentosComVaga:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, apartamento):
        if self.inicio is None:
            self.inicio = apartamento
            self.fim = apartamento
        else:
            self.fim.proximo = apartamento
            self.fim = apartamento

    def liberar_vaga(self):
        if self.inicio is None:
            return None
        liberado = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        liberado.proximo = None
        return liberado

    def imprimir(self):
        if self.inicio is None:
            print("Nenhum apartamento.")
        else:
            atual = self.inicio
            while atual is not None:
                atual.imprimir()
                atual = atual.proximo

    def contar_apartamentos_com_vaga(self):
        count = 0
        atual = self.inicio
        while atual is not None:
            if atual.vaga is not None:
                count += 1
            atual = atual.proximo
        return count
