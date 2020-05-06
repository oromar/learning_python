from random import randint

def lista_grande(n):
  lista = []
  for i in range(n):
    lista.append(randint(100, 9999999))
  return lista

if __name__=='__main__':
  print(lista_grande(100))
  