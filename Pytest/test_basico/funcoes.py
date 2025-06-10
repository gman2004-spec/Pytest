def tamanho_string(nome):
    tamanho = len(nome)
    return tamanho

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    total = 0
    
    for num in lista_numeros:
        total += num
        media = total / len(lista_numeros)
        return media
    
    