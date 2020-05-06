def conta_letras(frase, contar='vogais'):
    result = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(frase)):
        if frase[i] != ' ':
            if contar == 'vogais':
                if frase[i] in vogais:
                    result += 1
            else:
                if frase[i] not in vogais:
                    result += 1
    return result

print(conta_letras('quantas vogais tem aqui', contar='consoantes'))
