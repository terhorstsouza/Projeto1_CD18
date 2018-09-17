def limpa_texto(texto):
    lista = []

    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",\
            "q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",\
            "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",\
            "W","X","Y","Z", " "]
    for letra in texto:
        lista.append(letra)
        if letra not in letras:
            lista.remove(letra)

    final = ''.join(lista)
    return final


teste = 'comi uma banana'

print(limpa_texto(teste))