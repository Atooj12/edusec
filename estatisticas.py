from statistics import mode, median

def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

def calcular_moda(lista):
    try:
        return mode(lista)
    except:
        return "Sem moda"

def calcular_mediana(lista):
    return median(lista) if lista else 0
