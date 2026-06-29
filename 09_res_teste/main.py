import os

from jupyter_server.auth import passwd

"""



• 3 - Procurar produto

• 5 - Contar produtos
• 0 - Sair

"""
list_pordutos = ["Arroz", "Bananas", "Uvas"]


SIZE_SEPARADOR = 30

def separador(titulo:str = None, tamanho_linha:int = SIZE_SEPARADOR, char:str = "-"):
    if titulo:
        len_titulo = len(titulo)
        margem = (tamanho_linha - len_titulo) / 2
        left = margem.__floor__()-1 # arredonda para baixo
        right = margem.__ceil__()-1 # arredonda para cima

        print(char*left, titulo, char*right)
        return

    print(char*tamanho_linha)

def menu() -> str:
    os.system("clear")
    print("-"*30)
    print("1 - Adicionar produto")
    print("2 - Mostrar lista")
    print("3 - Procurar produto")
    print("4 - Remover produto")
    print("5 - Contar produtos")
    print("0 - Sair")
    print("-"*30)
    return input("Selecione uma opção: ")


# Pede o nome de um produto e adiciona-o à lista. Não devem ser aceites nomes vazios.
def adicionar_produto():


    separador(titulo="Adicionar produto", char="-")
    produto = input("Informe o nome do produto: ")
    if len(produto) == 0:
        print("o nome do porduto nao pode esta vazio")
        return

    list_pordutos.append(produto)


# Mostra todos os produtos existentes. Se a lista estiver vazia, apresenta uma mensagem
def mostrar_lista():

    separador(titulo="Lista de produtos", char="-")
    if len(list_pordutos) == 0:
        print("Lista vazia")
    else:

        for num, produto in enumerate(list_pordutos):
            print(f"porduto {num+1} - {produto}")

    separador()


def procurar_produto():

    separador(titulo="Procurar produto", char="-")
    produto = input("Informe o nome do produto: ")
    if len(produto) == 0:
        print("o nome do porduto nao pode esta vazio")
        return

    if produto in list_pordutos:
        print(f"{produto} Está na lista")
    else:
        print(f"{produto} não na lista")

    separador()


def remover_produto():
    separador(titulo="Remover produto", char="-")
    mostrar_lista()
    idx = input("Porduto a remover: ")

    if idx.isdigit():
        idx = int(idx)
        if idx < len(list_pordutos):
            pord = list_pordutos.pop(idx-1)
            print(f"{pord} removido com sucesso")
            return
        else:
            print("porduto nao existe")
            return


    if idx in list_pordutos:
        list_pordutos.remove(idx)
        print(f"{idx} removido com sucesso")
        return
    else:
        print("porduto nao existe")
        return


def contar_produtos():

    separador(titulo="Contar produtos", char="-")
    print(f"A Lista tem {len(list_pordutos)} produtos")
    separador()


while True:
    resp = menu()
    os.system("clear")

    match resp:
        case "1":
            adicionar_produto()

        case "2":
            mostrar_lista()

        case "3":
            procurar_produto()

        case "4":
            remover_produto()

        case "5":
            contar_produtos()

        case "0":
            print("Saindo do programa")
            break

        case _:
            print("opeção invalida")

    input("enter para continuar")