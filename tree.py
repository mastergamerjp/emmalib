class NodeTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

# from .NodeTree import NodeTree

class BinaryTree:
    
    @staticmethod
    def bifurcation(currentNode, value): # currentNode é onde ele ta, value é o valor que ele quer saber onde colocar
        # método que decide se deve ir para a esquerda ou direita
        return 'left' if currentNode.data > value else 'right'

    def __init__(self, root=None, method=bifurcation):
        self.root = root if root else None
        self.method = method
        self.nodesNumber = 1 if root else 0
        self.heigth = 1 if root else 0

    def printTree(self, currentNode=None, level=0):
        """Exibe a árvore no terminal"""
        # cria uma matriz com uma lista de listas de cada grau da árvore, cada listar termina em "\n", criando as camadas da árvore visualmente
        if not currentNode and level == 0:
            currentNode = self.root
        if currentNode is not None:
            self.printTree(currentNode.right,level+1)
            print(' '*level + f'->{currentNode.data}')
            self.printTree(currentNode.left, level+1)

        
        

    def isEmpty(self):
        return self.root is None
    
    def insert(self, data, currentNode=None):# ! apresentação
        """Insere um novo nó na árvore"""
        if self.root is None:
            self.root = NodeTree(data)
            return
        if not currentNode:
            currentNode = self.root
        choice = self.method(currentNode, data)
        if choice == 'left':
            if currentNode.left == None:
                currentNode.left = NodeTree(data)
                return
            self.insert(data, currentNode.left)
        elif choice == 'right':
            if currentNode.right == None:
                currentNode.right = NodeTree(data)
                return
            self.insert(data, currentNode.right)
        else:
            print("BINARY TREE ERROR")
        
    
    def search(self, data, node=None, first=True):
        """Retorna um nó da árvore que tenha um dado específico"""
        if first:
            node = node if node else self.root
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(data, node.left, False)
        else:
            return self.search(data, node.right, False)
    
    def deleteTree(self):
        self.root = None

    def getLeaf(self, currentNode=None, leafList=[]):# ! apresentação
        """Retorna uma lista com os valores dos nós folha da árvore"""
        if not currentNode:
            currentNode = self.root
        if currentNode.left:
            self.getLeaf(currentNode.left, leafList)
        if currentNode.right:
            self.getLeaf(currentNode.right, leafList)
        if not currentNode.left and not currentNode.right:
            leafList.append(currentNode.data)
        return leafList

    def getAncestors(self, data, path=None, currentNode=None, res=[]):# ! apresentação
        """Retorna a lista de ancestrais de um nó"""
        if len(res) != 0:
            return res
        
        if not path:
            currentNode = self.root
            path = []
            path.append(currentNode.data)
            if data == currentNode.data:
                res = [data]
                return res
        else:
            path.append(currentNode.data)
            
        if currentNode.data == data:
            res = [*path]
        
        if currentNode.left:
            res = self.getAncestors(data, path, currentNode.left, res)
            if len(path) > 0: path.pop()
        if currentNode.right:
            res = self.getAncestors(data, path, currentNode.right, res)
            if len(path) > 0: path.pop() 
        return res
    def getSuccessors(self, data):# ! apresentação
        """Retorna uma sub-árvore que tem como raíz um nó específico"""
        node = self.search(data)
        if node:
            return BinaryTree(node)
        else:
            return None
    
    def getParentAndSuccessors(self, data):# ! apresentação
        """Retorna uma sub-árvore que tem como raíz um nó específico e seu pai"""
        ancestors = self.getAncestors(data)
        successors = self.getSuccessors(data)
        
        if data == self.root.data:
            parent = None
        else:
            parent = ancestors[len(ancestors)-2]
        
        return [
            parent,
            successors
        ]
    
# f"{var:^x}"

# var = variavel
# ^ = centralizado
# x = tamanho