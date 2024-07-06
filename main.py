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
            torre_id = int(input("ID da torre: "))
            torre = next((torre for torre in torres if torre.id == torre_id), None)
            vaga = int(input("Número da vaga (ou -1 se não houver): "))

            apartamento = Apartamento(id, numero, vaga if vaga != -1 else None, torre)
            
            if torre.apartamento_existe(id, numero):
                print("Erro: Apartamento com o mesmo ID ou número já existe nesta torre.")
            else:
                torre.adicionar_apartamento(apartamento)
                if apartamento.vaga is not None:
                    lista_apartamentos.adicionar(apartamento)
                else:
                    fila_espera.adicionar(apartamento)

        elif opcao == 2:
            if lista_apartamentos.inicio is None:
                print("Nenhum apartamento com vaga de garagem disponível para liberar.")
                continue
            
            apartamento = lista_apartamentos.liberar_vaga()
            numero_vaga = apartamento.vaga
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
