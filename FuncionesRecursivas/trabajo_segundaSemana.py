l = [1,3,313,23,2,3,23]
def hacerContador(lista: list[int], idx: int = 0, contador: int = 0) -> int:
    if (len(lista) == idx):
        return contador 
    return hacerContador(lista, idx + 1, contador + 1)

print(hacerContador(l))
print(l)
