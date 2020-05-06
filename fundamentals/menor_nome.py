def menor_nome(palavras):
    for i in range(len(palavras)):
        palavras[i] = palavras[i].strip()
    menor = palavras[0]
    for i in range(1, len(palavras)):
        if len(palavras[i]) < len(menor):
               menor = palavras[i]

    return menor.capitalize()
               
               
