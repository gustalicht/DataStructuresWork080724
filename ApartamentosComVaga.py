class ListaApartamentosComVaga:
    def __init__(self):
        self.inicio = None
        self.contagem_vagas = 0  # Contador para o número de apartamentos com vaga

    def adicionar_com_vaga(self, apartamento):
        if self.inicio is None or self.inicio.vaga > apartamento.vaga:
            apartamento.proximo = self.inicio
            self.inicio = apartamento
        else:
            atual = self.inicio
            while atual.proximo is not None and atual.proximo.vaga < apartamento.vaga:
                atual = atual.proximo
            apartamento.proximo = atual.proximo
            atual.proximo = apartamento
        self.contagem_vagas += 1  # Incrementa o contador de vagas ocupadas

    def adicionar_sem_vaga(self, apartamento):
        if self.inicio is None:
            self.inicio = apartamento
        else:
            fim = self.inicio
            while fim.proximo is not None:
                fim = fim.proximo
            fim.proximo = apartamento

    def liberar_vaga(self, numero_vaga):
        if self.inicio is None:
            return None
        if self.inicio.vaga == numero_vaga:
            liberado = self.inicio
            self.inicio = self.inicio.proximo
            liberado.proximo = None
            self.contagem_vagas -= 1
            return liberado
        atual = self.inicio
        while atual.proximo is not None and atual.proximo.vaga != numero_vaga:
            atual = atual.proximo
        if atual.proximo is None:
            return None
        liberado = atual.proximo
        atual.proximo = atual.proximo.proximo
        liberado.proximo = None
        self.contagem_vagas -= 1
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
        return self.contagem_vagas
