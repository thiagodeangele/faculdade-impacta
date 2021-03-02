'''
Pilha

Dados armazenados:
	- Sequência arbitrária de dados

Operações fornecidas:
	- Criar estrutura
	- Inserir no topo
	- Remover do topo
	- Consultar o topo sem remover
	- Consultar tamanho (número de elementos)
'''

class Pilha:
    def __init__(self):
        self.pilha = []
        self.tamanho = 0
    
    def insere(self, novo):
        self.pilha.append(novo)
        self.tamanho += 1
    
    def remove(self):
        self.tamanho -= 1
        return self.pilha.pop() #pop remove o último elemento
    
    def topo(self):
        return self.pilha[-1]
    
    def __len__(self):
        return self.tamanho


p = Pilha()
p.insere (101)
p.insere (102)
p.insere (103)
print(p.remove())

print(f'A pilha está com tamanho {len(p)}')
print(f'No topo está o elemento {p.topo()}')




def imprime_invertido(mensagem):
    pilha = Pilha()
    for c in mensagem:
        pilha.insere(c)
    while len(pilha) > 0:
        c = pilha.remove()
        print(c, end='')
    print()

imprime_invertido('abc')
imprime_invertido('MIRIM')
imprime_invertido('Estou testando a informação invertida.')