'''
A Fila terá a seguinte especificação:

Dados armazenados:
    . Sequência arbitrária de dados.

Operações fornecidas:
    . Criar estrutura
    . Inserir no fim da fila
    . Remover do início da fila
    . Saber o tamanho
    . Verificar o primeiro sem remover

/////////////////////////////////////////////////////////////////

Vamos fazer as operações:

	1. Criar fila F
	2. Inserir em F o elemento 41
	3. Inserir em F o elemento 85
	4. Inserir em F o elemento 29
	5. Remover um elemento F
	6. Inserir em F o elemento 56
	7. Verificar o tamanho de F

Verificar quem é o primeiro da fila (o mais antigo)
'''

from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, novo):
        self.fila.append(novo)

    def remove(self):
        return self.fila.popleft()
    
    def __len__(self):
        return len(self.fila)
    
    def proximo(self):
        prox = self.fila.popleft()
        self.fila.append(prox)
        return prox

F = Fila()
F.insere(1)
F.insere(2)
F.insere(3)
print(F.fila)
print(f'Removi o elemento {F.remove()}')
F.insere(4)
print(f'A fila tem o tamanho {len(F)}')
print(F.fila)
print(f'O primeiro da fila é {F.proximo()}')