def busca(lista, elemento):
  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return False

def testa_busca():
  assert busca([1, 2, 3], 3) == 2
  assert busca([1, 2, 3], 4) == False
  assert busca([1, 2, 3], -1) == False
  print('testa_busca: Todos os testes passaram')

if __name__=='__main__':
  testa_busca()