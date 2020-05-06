def busca(lista, elemento):
  max = len(lista)-1
  min = 0
  while min <= max:    
    meio = (min + max)//2  
    print(meio)
    if lista[meio] == elemento:
      return meio
    elif elemento < lista[meio]:
      max = meio-1
    else: 
      min = meio+1
  return False

# def test_busca():
#   assert busca(['a', 'e', 'i'], 'e') == 1
#   assert busca([1, 2, 3, 4, 5], 6) == False
#   assert busca([1, 2, 3, 4, 5, 6], 4) == 3
#   print ('busca: Todos os testes passaram')

# if __name__=='__main__':
#   test_busca()
