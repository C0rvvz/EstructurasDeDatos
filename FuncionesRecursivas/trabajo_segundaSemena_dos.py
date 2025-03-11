"""
---

### 1. **Sumatoria de una lista**
   Implementa una función recursiva que reciba una lista de números y devuelva la suma de todos sus elementos.

   ```python
   def sumatoria(lista):
       pass
   ```

   **Ejemplo:**
   ```python
   sumatoria([1, 2, 3, 4, 5])  # Output: 15
   sumatoria([10, -5, 7])      # Output: 12
   ```

"""

"""

lista1 = [10, -5, 7]
lista2 = [1, 2, 3, 4, 5]

def sumatoria(lista):
  resultado = []
  for elemento in range(len(lista)):
    resultado.append(lista[elemento] + elemento)
  return resultado

print(sumatoria(lista1))
print(sumatoria(lista2))

"""
"""
---

### 2. **Contar elementos en una lista anidada**
   Escribe una función recursiva que cuente el número total de elementos en una lista, considerando que puede contener sublistas anidadas.

   ```python
   def contar_elementos(lista):
       pass
   ```

   **Ejemplo:**
   ```python
   contar_elementos([1, [2, 3], [4, [5, 6]]])  # Output: 6
   contar_elementos([[], [1, [2, 3]], 4])      # Output: 4
   ```

"""

"""
def contar_elementos(lista):
    if not lista:
        return 0
    contador = 0

    for elemento in lista:
        if isinstance(elemento, list): 
            contador += contar_elementos(elemento)
        else:
            contador += 1

    return contador

print(contar_elementos([1, [2, 3], [4, [5, 6]]]))  # Output: 6
"""

"""
---

### 3. **Número de dígitos de un número**
   Implementa una función recursiva que cuente cuántos dígitos tiene un número entero positivo.

   ```python
   def contar_digitos(n):
       pass
   ```

   **Ejemplo:**
   ```python
   contar_digitos(12345)   # Output: 5
   contar_digitos(987654)  # Output: 6
   ```
"""

"""
def contar_digitos(n, c = 0):
    if n == 0:
        return c
    else:
        return contar_digitos(n // 10, c + 1)
print(contar_digitos(10))
"""

"""
---

### 4. **Producto de dos números usando sumas**
   Implementa una función recursiva para calcular el producto de dos números enteros positivos utilizando solo sumas.

   ```python
   def producto(a, b):
       pass
   ```

   **Ejemplo:**
   ```python
   producto(3, 4)   # Output: 12
   producto(5, 6)   # Output: 30
   ```

"""

"""
def producto (a,b):
    if b == 0:
        return 0
    return a + producto(a,b-1)
print(producto(3,4))
"""

"""
---

### 5. **Comprobar si una palabra es palíndromo**
   Escribe una función recursiva que determine si una cadena es un palíndromo.

   ```python
   def es_palindromo(cadena):
       pass
   ```

   **Ejemplo:**
   ```python
   es_palindromo("radar")     # Output: True
   es_palindromo("reconocer") # Output: True
   es_palindromo("python")    # Output: False
   ```
"""

"""
def es_palindromo(cadena):
    palabra = ""
    for i in cadena:
        palabra = i + palabra
    
    if cadena == palabra:
        return True
    else:
        return False

print(es_palindromo("hola"))
"""