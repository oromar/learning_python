def ordenada(lista):
  aux = sorted(lista)
  for i in range(len(lista)):
    if lista[i] != aux[i]:
      return False
  return True

def testa_ordenada():
  assert ordenada([1, 2, 3]) == True
  assert ordenada([3, 2, 1]) == False
  assert ordenada([2,1,3]) == False
  print('testa_ordenada: Todos os testes passaram')

if __name__=='__main__':
  testa_ordenada()

