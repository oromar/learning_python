def encontra_impares(lista):
  r = []
  if len(lista) > 0:
    x = lista[0]
    if x % 2 != 0:
      r.append(x)
    r = r + encontra_impares(lista[1:])
  return r
      
# def test_encontra_impares():
#   assert encontra_impares([2,3,5]) == [3,5]
#   assert encontra_impares([2,3,5,6,7,8]) == [3,5,7]
#   assert encontra_impares([2,3,5,8,17]) == [3,5,17]
#   assert encontra_impares([2,3,5, 15, 14]) == [3,5,15]
#   print('encontra_impares:Todos os testes passaram')

# if __name__=='__main__':
#   test_encontra_impares()
  
  