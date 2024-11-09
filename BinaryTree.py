class NodeTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.data

# from .NodeTree import NodeTree

class BinaryTree:
    
    @staticmethod
    def bifurcation():
        # método que decide se deve ir para a esquerda ou direita
        pass

    def __init__(self, root=None, method=bifurcation):
        self.root = NodeTree(root) if root else None
        
    def __str__(self):
        # cria uma matriz com uma lista de listas de cada grau da árvore, cada listar termina em "\n", criando as camadas da árvore visualmente
        pass

    def isEmpty(self):
        return self.root is None
    
    def insert():
        pass
    
    def search():
        pass
    
    def printInOrder(self, node):
        pass
    
    def printPreOrder(self, node):
        pass
    
    def printPostOrder(self, node):
        pass
    
    def minNode(self, node):
        pass
    
    def maxNode(self, node):
        pass
    
    def heightTree(self, node):
        pass
    
    def countNodes(self, node):
        pass
    
    def delete(self, node, data):
        pass
    
    def deleteTree(self):
        self.root = None

    
# f"{var^x}"

# var = variavel
# ^ = centralizado
# x = tamanho
