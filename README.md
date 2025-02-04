# Data Structures Work

## O Conceito de Fila (FIFO)

FIFO significa **First In, First Out** (o primeiro a entrar é o primeiro a sair). As inserções de elementos são realizadas no final da fila e as exclusões de elementos são realizadas no início da fila.

## Fila

A fila é uma estrutura de dados que armazena um conjunto de elementos na sequência em que eles chegam na fila. Esta estrutura permite alocação dinâmica de memória e é constituída por elementos que possuem uma estrutura composta de valor e endereço do próximo elemento. Se estivermos no último elemento da fila, o campo para o endereço do próximo elemento terá como valor: `None`.

## Funcionamento do Código

Este projeto implementa a gestão de apartamentos em um condomínio, utilizando o conceito de fila (FIFO) para gerenciar a alocação e liberação de vagas de garagem. O código consiste em várias classes, cada uma com responsabilidades específicas. Abaixo está uma descrição detalhada de cada componente do código.

### Classes e Estruturas

#### Classe `Apartamento`

A classe `Apartamento` representa um apartamento com atributos como `id`, `numero`, `vaga`, `torre`, e `proximo`.

def cadastrar(self, novo_apartamento):
    if self.proximo is None:
        self.proximo = novo_apartamento
    else:
        self.proximo.cadastrar(novo_apartamento)


Construtor: Inicializa os atributos do apartamento.
cadastrar: Adiciona um novo apartamento na lista encadeada.
imprimir: Imprime os detalhes do apartamento.

### Classe ListaApartamentosComVaga
A classe ListaApartamentosComVaga gerencia a lista encadeada de apartamentos, tanto com vaga quanto na fila de espera.

def liberar_vaga(self):
    if self.inicio is None:
        return None
    liberado = self.inicio
    self.inicio = self.inicio.proximo
    if self.inicio is None:
        self.fim = None
    liberado.proximo = None
    return liberado

Construtor: Inicializa a fila com inicio e fim como None.
adicionar: Adiciona um apartamento ao fim da fila.
liberar_vaga: Remove sempre o primeiro apartamento da fila.
imprimir: Imprime todos os apartamentos na lista.
contar_apartamentos_com_vaga: Conta quantos apartamentos têm vaga de garagem.

### Classe Torre
A classe Torre representa uma torre de apartamentos com atributos como id, nome, endereco, e uma lista de apartamentos.

def apartamento_existe(self, id, numero):
    for apartamento in self.apartamentos:
        if apartamento.id == id or apartamento.numero == numero:
            return True
    return False


Construtor: Inicializa os atributos da torre.
adicionar_apartamento: Adiciona um apartamento à lista de apartamentos da torre.
apartamento_existe: Verifica se um apartamento com o mesmo id ou numero já existe na torre.


### Funcionalidade Principal
O arquivo main.py contém a lógica principal do programa, gerenciando a interação com o usuário e chamando as funções apropriadas para gerenciar os apartamentos e vagas de garagem.

Exibir Menu: Exibe as opções do menu para o usuário.
### Inicialização das Torres: 

Cria três instâncias da classe Torre, cada uma representando uma torre de apartamentos.

## Inicialização das Listas:
lista_apartamentos é uma instância de ListaApartamentosComVaga, gerenciando apartamentos com vaga.

## fila_espera : 
é uma instância de ListaApartamentosComVaga, gerenciando a fila de espera dos apartamentos sem vaga.
### Adicionar Apartamento:
Solicita as informações do apartamento (ID, número, torre, vaga).
Verifica se o apartamento já existe na torre escolhida.
Se não existir, adiciona o apartamento à torre.
Se o apartamento tem vaga, é adicionado à lista de apartamentos com vaga (lista_apartamentos).
Se o apartamento não tem vaga, é adicionado à fila de espera (fila_espera).
## Liberar Vaga:
Remove sempre o primeiro apartamento da lista de apartamentos com vaga.
Atribui a vaga liberada ao primeiro apartamento na fila de espera e o adiciona à lista de apartamentos com vaga.
Mostrar Apartamentos com Vaga: Imprime a lista de apartamentos com vaga de garagem.
Mostrar Fila de Espera: Imprime a fila de espera dos apartamentos sem vaga de garagem.
Sair: Encerra o programa.

## Como Executar
Para executar o programa, basta rodar o script main.py em um ambiente Python. O programa fornecerá um menu interativo para gerenciar os apartamentos e vagas de garagem.

_______________________________________________________________________________________
