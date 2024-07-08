from Torre import Torre
from Apartamento import Apartamento
from ApartamentosComVaga import ListaApartamentosComVaga

def exibir_menu():
    print("1. Adicionar apartamento")
    print("2. Liberar vaga de garagem")
    print("3. Mostrar apartamentos com vaga")
    print("4. Mostrar fila de espera")
    print("5. Sair")

def main():
    torres = [
        Torre(1, "Torre 1", "Endereço 1"),
        Torre(2, "Torre 2", "Endereço 2"),
        Torre(3, "Torre 3", "Endereço 3"),
    ]

    lista_apartamentos = ListaApartamentosComVaga()
    fila_espera = ListaApartamentosComVaga()

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            id = int(input("ID do apartamento: "))
            numero = input("Número do apartamento: ")
            print("Torres disponíveis:")
            for torre in torres:
                print(f"{torre.id} - {torre.nome}")
            id_torre = int(input("Escolha o ID da torre: "))
            torre_selecionada = next((torre for torre in torres if torre.id == id_torre), None)
            if not torre_selecionada:
                print("Torre inválida.")
                continue

            if lista_apartamentos.contar_apartamentos_com_vaga() < 10:
                numero_vaga = int(input("Número da vaga: "))
                apartamento = Apartamento(id, numero, numero_vaga, torre_selecionada)
                lista_apartamentos.adicionar(apartamento)
                print(f"Apartamento {numero} cadastrado com a vaga {numero_vaga}.")
            else:
                apartamento = Apartamento(id, numero, torre=torre_selecionada)
                fila_espera.adicionar(apartamento)
                print(f"Apartamento {numero} adicionado à fila de espera.")

        elif opcao == 2:
            numero_vaga = int(input("Número da vaga a ser liberada: "))
            apartamento = lista_apartamentos.liberar_vaga()
            if apartamento:
                print(f"Apartamento {apartamento.numero} liberou a vaga {numero_vaga}.")
                
                if fila_espera.inicio is not None:
                    novo_apartamento = fila_espera.liberar_vaga()
                    if novo_apartamento:
                        novo_apartamento.vaga = numero_vaga
                        lista_apartamentos.adicionar(novo_apartamento)
                        print(f"Apartamento {novo_apartamento.numero} da fila de espera agora tem a vaga {numero_vaga}.")

        elif opcao == 3:
            print("Apartamentos com vaga de garagem:")
            lista_apartamentos.imprimir()

        elif opcao == 4:
            print("Fila de espera por vagas de garagem:")
            fila_espera.imprimir()

        elif opcao == 5:
            break

if __name__ == "__main__":
    main()
