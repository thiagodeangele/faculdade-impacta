'''
Armazenar os dados:

- Nome
- Idade
- Altura
- Peso
- Tipo Sanguínio (se conhecido)
- Queixa no PS (se houver)
- Datas de Consulta

Operações:

- Alterar idade
- Alterar peso
- Alterar queixa
- Adicionar uma data de consulta

'''

class Paciente:
    def __init__(self, nome, idade, peso, altura, queixa=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.queixa = queixa
        self.altura = altura
        self.consultas = []
        self.tipo_sanguineo = []


    def altera_idade(self, nova_idade): # Self é o objeto modificado
        self.idade = nova_idade
    
    def adidiona_consulta(self, data_da_consulta):
        self.consultas.append(data_da_consulta)
    
    

p = Paciente('Thiago', 35, 90, 1.75)
p.adidiona_consulta('24/02/2019')
p.adidiona_consulta('26/02/2020')
p.adidiona_consulta('01/02/2021')

print(p.peso)