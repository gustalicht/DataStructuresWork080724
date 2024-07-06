class ListaApartamentosComVaga:
    def __init__(self):
        self.topo = None

    def adicionar(self, apartamento):
        if self.topo is None or self.topo.vaga > apartamento.vaga:
            apartamento.proximo = self.topo
            self.topo = apartamento
        else:
            atual = self.topo
            while atual.proximo is not None and atual.proximo.vaga < apartamento.vaga:
                atual = atual.proximo
            apartamento.proximo = atual.proximo
            atual.proximo = apartamento

    def liberar_vaga(self, numero_vaga):
        if self.topo is None:
            return None
        if self.topo.vaga == numero_vaga:
            liberado = self.topo
            self.topo = self.topo.proximo
            liberado.proximo = None
            return liberado
        atual = self.topo
        while atual.proximo is not None and atual.proximo.vaga != numero_vaga:
            atual = atual.proximo
        if atual.proximo is None:
            return None
        liberado = atual.proximo
        atual.proximo = atual.proximo.proximo
        liberado.proximo = None
        return liberado

    def imprimir(self):
        if self.topo is None:
            print("Nenhum apartamento com vaga de garagem.")
        else:
            print("Apartamentos com vaga de garagem:")
            atual = self.topo
            while atual is not None:
                print(f"Apartamento {atual.numero} - Vaga: {atual.vaga}")
                atual = atual.proximo

    def contar_apartamentos_com_vaga(self):
        count = 0
        atual = self.topo
        while atual is not None:
            if atual.vaga is not None:
                count += 1
            atual = atual.proximo
        return count