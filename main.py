from stack import Stack

def menu():
    print("\n==== Menu Stack Ativ 3 ====")
    print("1. Empilhar (push)")
    print("2. Desempilhar (pop)")
    print("3. Mostrar elementos da pilha")
    print("4. Mostrar quantidade de elementos")
    print("0. Sair")

pilha = Stack()

while True:
    menu()
    op = input("Opcao desejada: ")

    if op == "1":
        item = input("Digite o numero ou o nome que quer empilhar: ")
        pilha.push(item)
        print(f"Pronto. O elemento '{item}' foi empilhado!")

    elif op == "2":
        deleted = pilha.pop()
        if deleted is not None:
            print(f"Pronto. O item '{deleted}' foi removido!")
        else:
            print("Pilha vazia! Nao ha como desempilhar")

    elif op == "3":
        itens = pilha.show()

        if pilha.top != 0:
            print("Elementos da pilha: ")
            print(itens)
        else: 
            print("Pilha vazia. Nao ha elementos para mostrar")

    elif op == "4":
        print("A quantidade de elementos da pilha eh", pilha.size())

    elif op == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opcao invalida. Tente novamente!")