class Node:
  def __init__(self, valor):
    self.info = valor
    self.prox = None

class PilhaEnc:
  def __init__(self):
    self.topo = None
  
  def inserir(self, dado):
    new_node = Node(dado)
    new_node.prox = self.topo
    self.topo = new_node
        
  def remover(self):
    if (self.topo != None):
      self.topo = self.topo.prox

  
  def consult(self):
    if (self.topo != None):
      return self.topo.info
    else:
      return None
    


