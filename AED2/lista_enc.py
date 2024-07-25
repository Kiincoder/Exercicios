class Node:
  def __init__(self, dado = None):
    self.dado = dado
    self.prox = None

class ListaEnc:
  def __init__(self):
    self.init = Node()
  
  def append(self, dado):
    new_node = Node(dado)
    ptAux = self.init
    while ptAux.prox != None:
      ptAux = ptAux.prox
    ptAux.prox = new_node

  def print(self):
    elements = []
    cur_node = self.init
    while cur_node.prox != None:
      cur_node = cur_node.prox
      elements.append(cur_node.dado)
    print(elements)

