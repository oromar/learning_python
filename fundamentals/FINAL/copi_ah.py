import re
import sys

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")
  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    x = 0
    for i in range(len(as_a)):
        x += abs(as_a[i] - as_b[i])
    
    return x / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tamanho_medio_palavras = 0
    soma_tamanho_palavras = 0
    soma_palavras = 0
    soma_frases = 0
    type_token = 0
    soma_caracteres_sentencas = 0
    soma_caracteres_frases = 0

    sentencas = []
    frases = []
    palavras = []

    sentencas = separa_sentencas(texto)
    for i in range(0, len(sentencas)):
        soma_caracteres_sentencas += len(sentencas[i]) - 1
        frases = separa_frases(sentencas[i])
        soma_frases += len(frases)
        for j in range(0, len(frases)):
            soma_caracteres_frases += len(frases[j]) - 1
            palavras = separa_palavras(frases[j])
            soma_palavras += len(palavras)
            for k in range(0, len(palavras)):
                soma_tamanho_palavras += len(palavras[k])

    tamanho_medio_palavras = soma_tamanho_palavras / soma_palavras
    type_token = n_palavras_diferentes(palavras) / soma_palavras
    hapax_legomana = n_palavras_unicas(palavras) / soma_palavras
    tamanho_medio_sentenca = soma_caracteres_sentencas / len(sentencas)
    complexidade_sentenca = len(frases) / len(sentencas)
    tamanho_medio_frase = soma_caracteres_frases / soma_frases

    return [tamanho_medio_palavras, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase ]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    a = 999999999999
    z = 1
    for i in range(len(textos)):
        x = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if x < a:
            a = x
            z = i + 1
    return z 

def main():
  assinatura = le_assinatura()
  textos = le_textos()
  x = avalia_textos(textos, assinatura)
  print('O autor do texto', x,'está infectado com COH-PIAH')

main()  
  
