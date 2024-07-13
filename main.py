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

    lista_apartamentos_com_vaga = ListaApartamentosComVaga()
    fila_espera = ListaApartamentosComVaga()

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            while True:
                try:
                    print("Torres disponíveis:")
                    for torre in torres:
                        print(f"{torre.id} - {torre.nome}")
                    torre_id = int(input("ID da torre: "))
                    if torre_id not in [1, 2, 3]:
                        print("Torre não encontrada. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, tente novamente.")
            torre = next((torre for torre in torres if torre.id == torre_id), None)
            id = int(input("ID do apartamento: "))
            if torre.id_existe(id):
                print("Erro: Apartamento com o mesmo ID já existe nesta torre.")
            numero = input("Número do apartamento: ")
            if torre.numero_existe(numero):
                print("Erro: Apartamento com o mesmo numero já existe nesta torre.")

            if lista_apartamentos_com_vaga.contar_apartamentos_com_vaga() < 10:
                vaga = int(input("Número da vaga (ou -1 se não houver): "))
            else:
                print("Todas as vagas de garagem estão ocupadas, você irá diretamente para a fila de espera")
                apartamento = Apartamento(id,numero,vaga == None, torre)
                fila_espera.adicionar_sem_vaga(apartamento)
                print("Apartamento adicionado a fila de espera!")

            apartamento = Apartamento(id, numero, vaga if vaga != -1 else None, torre)
            torre.adicionar_apartamento(apartamento)
            if apartamento.vaga is not None and lista_apartamentos_com_vaga.contar_apartamentos_com_vaga() < 10:
                print("Apartamento adicionado a Torre!")
                lista_apartamentos_com_vaga.adicionar_com_vaga(apartamento)

        elif opcao == 2:
            if lista_apartamentos_com_vaga.inicio is None:
                print("Nenhum apartamento com vaga de garagem disponível para liberar.")
                continue
            
            numero_vaga = int(input("Número da vaga a ser liberada: "))
            apartamento = lista_apartamentos_com_vaga.liberar_vaga(numero_vaga)
            if apartamento is None:
                print(f"Vaga {numero_vaga} não encontrada.")
                continue
            numero_vaga = apartamento.vaga
            print(f"Apartamento {apartamento.numero} liberou a vaga {numero_vaga}.")
            
            if fila_espera.inicio is not None:
                novo_apartamento = fila_espera.inicio
                fila_espera.inicio = fila_espera.inicio.proximo
                if fila_espera.inicio is None:
                    fila_espera.fim = None
                novo_apartamento.vaga = numero_vaga
                novo_apartamento.proximo = None
                lista_apartamentos_com_vaga.adicionar_com_vaga(novo_apartamento)
                print(f"Apartamento {novo_apartamento.numero} da fila de espera agora tem a vaga {numero_vaga}.")
                fila_espera.contagem_vagas -= 1
                fila_espera.adicionar_sem_vaga(apartamento)

        elif opcao == 3:
            print("Apartamentos com vaga de garagem:")
            lista_apartamentos_com_vaga.imprimir()

        elif opcao == 4:
            print("Fila de espera por vagas de garagem:")
            fila_espera.imprimir()

        elif opcao == 5:
            break

if __name__ == "__main__":
    main()
