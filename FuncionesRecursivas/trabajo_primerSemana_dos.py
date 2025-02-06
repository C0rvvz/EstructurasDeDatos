import random

class Perona():
    def __init__(self):
        self.name = random.choice(["Jorge","Maria","Pedro","Juan"])
        self.edad = random.randint(0,100)
    
    def __repr__(self):
        return f"{self.name} tiene {self.edad} años"
    
    def saludar(self):
        return f"Hola {self.name} de {self.edad} años"
    
personas = [[Perona() for fila in range(4)] for columna in range(4)]

personasAplanadas = [persona for fila in personas for persona in fila]

personasAplanadas.sort(key=lambda persona: persona.edad, reverse=True)

for i in range(len(personasAplanadas) - 1):
    print(personasAplanadas[i].saludar(), "y", personasAplanadas[i+1].saludar())

print("--------------------------------------------------")
for fila in personas:
    print(fila)
