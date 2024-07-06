from ApartamentosComVaga import ListaApartamentosComVaga
from FilaEspera import FilaEspera
from Apartamento import Apartamento
from Torre import Torre
def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar apartamento")
    print("2. Liberar vaga de garagem")
    print("3. Imprimir lista de apartamentos com vaga")
    print("4. Imprimir fila de espera por vaga de garagem")
    print("5. Sair")

def main():
    lista_apartamentos = ListaApartamentosComVaga()
    fila_espera = FilaEspera()
    torres = [
         Torre(1, "Torre A", "Endereço A"),
        Torre(2, "Torre B", "Endereço B"),
        Torre(3, "Torre C", "Endereço C")
    ]

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            id = int(input("ID do apartamento: "))
            numero = int(input("Número do apartamento: "))
            print("Torres disponíveis:")
            for torre in torres:
                print(f"{torre.id}. {torre.nome} - {torre.endereco}")
            torre_id = int(input("ID da torre: "))
            vaga = int(input("Número da vaga de garagem (ou -1 se não tiver): "))
            torre = next((torre for torre in torres if torre.id == torre_id), None)
            if torre is None:
                print("Torre não encontrada.")
                continue
            if torre.apartamento_existe(id, numero):
                print("Erro: ID ou número do apartamento já existente na torre.")
                continue
            if torre.quantidade_apartamentos() >= 10:
                print("Erro: Torre já possui 10 apartamentos.")
                continue
            apartamento = Apartamento(id, numero, vaga if vaga != -1 else None, torre)
            torre.adicionar_apartamento(apartamento)
            if vaga == -1 or lista_apartamentos.contar_apartamentos_com_vaga() >= 10:
                fila_espera.adicionar(apartamento)
            else:
                lista_apartamentos.adicionar(apartamento)
                
        elif opcao == 2:
            numero_vaga = int(input("Número da vaga a ser liberada: "))
            liberado = lista_apartamentos.liberar_vaga(numero_vaga)
            if liberado is not None:
                fila_espera.adicionar(liberado)
                novo_apartamento = fila_espera.remover()
                if novo_apartamento is not None:
                    novo_apartamento.vaga = numero_vaga
                    lista_apartamentos.adicionar(novo_apartamento)
                print("Vaga liberada e novo apartamento alocado.")
            else:
                print("Vaga não encontrada.")

        elif opcao == 3:
            lista_apartamentos.imprimir()

        elif opcao == 4:
            fila_espera.imprimir()

        elif opcao == 5:
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
