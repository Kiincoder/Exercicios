from pilha_enc import PilhaEnc
from fila_enc import FilaEnc

def sortFila(fila):
    pilha_ord = PilhaEnc()
    pilha_aux = PilhaEnc()

    while fila.consultar() != None:
        topo_pilha_ord = pilha_ord.consult()
        topo_pilha_aux = pilha_aux.consult()
        inicio_fila = fila.consultar()

        if topo_pilha_ord != None:
            if topo_pilha_ord >= inicio_fila:
                pilha_ord.inserir(inicio_fila)

            else:
                while topo_pilha_ord != None and inicio_fila > topo_pilha_ord:
                    pilha_aux.inserir(topo_pilha_ord)
                    pilha_ord.remover()

                pilha_ord.inserir(inicio_fila)

                while topo_pilha_aux != None:
                    pilha_ord.inserir(topo_pilha_aux)
                    pilha_aux.remover()
        else:
            pilha_ord.inserir(inicio_fila)
        
        fila.remover()

    # Montar a fila:
    while pilha_ord.consult() != None:
        fila.inserir(pilha_ord.consult())
        pilha_ord.remover()

a = FilaEnc()
a.inserir(10)
a.inserir(3)
a.inserir(100)
a.inserir(16)
a.inserir(5)
a.inserir(30)
a.inserir(1)


sortFila(a)

while a.consultar() != None:
    print(a.consultar())
    a.remover()