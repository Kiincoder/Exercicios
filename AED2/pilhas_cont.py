class Pilhacont:
    def __init__(self, size):
        self.vetor = [None] * size
        self.lim = size - 1
        self.base = 0
        self.top = self.base - 1

    def inserir(self, element):
        if (self.top < self.lim):
            self.top += 1
            self.vetor[self.top] = element
            return True
        else:
            return False

    def remover(self):
        if (self.top >= self.base):
            self.top -= 1
            return True
        else:
            return False

    def destruir(self):
        self.top = self.base - 1

    def consulta(self):
        return self.vetor[self.top]


pilha = Pilhacont(10)
pilha.inserir(1)
pilha.inserir(2)
pilha.inserir(3)
print(f"topo da pilha = {pilha.consulta()}")
pilha.destruir()
print(f"topo da pilha = {pilha.consulta()}")



# print("Pilha vazia")
# print(20*"=")

# pilha.print()
# print(20*"=")
# print("Pilha com algo inserido")
# for i in range(1,8):
#     pilha.inserir(i)
# pilha.print()
# print(20*"=")
# for i in range(1,5):
#     pilha.remover()
# pilha.print()