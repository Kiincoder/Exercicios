class Nodo ():
    def __init__ (self, valor):
        self.info = valor
        self.prox = None

class FilaEnc:
    def __init__ (self):
        self.ini = None
        self.fim = None

    def inserir (self, valor):
        elem = Nodo(valor)
        
        if self.ini == None and self.fim == None:
            self.ini = elem
        else:
            self.fim.prox = elem

        self.fim = elem

    def consultar (self):
        if self.ini != None:
            return self.ini.info

        
    def remover (self):
        if self.ini != None:
            if self.ini == self.fim:
                self.fim = None

            self.ini = self.ini.prox








