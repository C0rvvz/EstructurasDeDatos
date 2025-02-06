import random

class Persona:
   def __init__(self):
    self.nombre = random.choice(["Juna","Juan","Ana"])
    self.edad =  random.randint (18,90)

   def __repr__(self):
     return f"nombre: {self.nombre}, edad: {self.edad}" 

   def  saludar(self):
    return f"Hola {self.nombre} de {self.edad}"

personas = []

for _ in range(5):
  persona = Persona()
  personas.append(persona)

personaMayor = personas[0]

for persona in personas:
  if persona.edad > personaMayor.edad:
    personaMayor = persona

print(personas)
print("---------------------------------------------------------------")

personas.sort(key=lambda persona: persona.edad, reverse=True)
print(personas)

for i in range(len(personas) - 1):
  print(personas[i].saludar(), "y", personas[i+1].saludar())
  

