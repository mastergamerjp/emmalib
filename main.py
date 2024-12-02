# 2. Faça um programa para executar as operações abaixo em uma árvore binária.
# Menu
# 1 – Inserir número
# 2 – Mostrar nós folha
# 3 – Mostrar os nós ancestrais de um nó
# 4 – Mostrar os descendentes de um nó
# 5 – Mostrar o nó pai e os nós filhos de um nó
# 6 – Sair


from tree import BinaryTree, NodeTree


def main():
    binaryTree = BinaryTree()
    while True:
        print('''
        ======== Árvore Binária ========
        Menu
        [1] - Inserir número
        [2] - Mostrar nós folha
        [3] - Mostrar os nós ancestrais de um nó
        [4] - Mostrar os descendentes de um nó
        [5] - Mostrar o nó pai e os nós filhos de um nó
        [6] - Sair
              ''')
        code = input("Digite o código da ação: ")
        if code == "1":
            value = None
            while True:
                try:
                    value = float(input("Digite o número a ser inserido na árvore: "))
                    break
                except:
                    print("Valor inválido, deve ser um número")
                    continue
            binaryTree.insert(value)
            binaryTree.printTree()
        elif code == "2":
            print("Nós-folha: {}".format(binaryTree.getLeaf()))
        elif code == "3":
            value
            while True:
                try:
                    value = float(input("Digite o número que deseja ver os ancestrais: "))
                    break
                except:
                    print("Valor inválido, deve ser um número")
                    continue
            print("Nós ancestrais de {}: {}".format(value, binaryTree.getAncestors(value)))
        elif code == "4":
            value
            while True:
                try:
                    value = float(input("Digite o número que deseja ver os descendentes: "))
                    break
                except:
                    print("Valor inválido, deve ser um número")
                    continue
            binaryTree.getSuccessors(value).printTree()
        elif code == "5":
            value
            while True:
                try:
                    value = float(input("Digite o número que deseja ver o pai e filhos do nó: "))
                    break
                except:
                    print("Valor inválido, deve ser um número")
                    continue
            temp = binaryTree.getParentAndSuccessors(value)
            print('''
        Nó pai: {}
        Nós descendentes:'''.format(temp[0]))
            temp[1].printTree()
        elif code == "6":
            break
        else:
            print('''
        ===========================================
        Código inválido, por favor tente novamente.
        ===========================================
        ''')
main()



# zot = BinaryTree()
# zot.insert(2)
# zot.insert(2)
# zot.insert(3)
# zot.insert(2.5)
# zot.insert(4)
# zot.insert(1)
# zot.insert(-2)

# zot.printTree()

# print(zot.getLeaf())
# print(zot.getAncestors(4))

# print(zot.search(3))


# print(zot.getSuccessors(3).printTree())

# print(zot.getParentAndSuccessors(3))