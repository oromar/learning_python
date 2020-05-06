def soma_lista(lista):
  if len(lista) == 1:
    return lista[0]    
  else:
    return lista[-1] + soma_lista(lista[:len(lista)-1])

# def test_soma_lista():
#   assert soma_lista([1]) == 1
#   assert soma_lista([2]) == 2
#   assert soma_lista([3]) == 3
#   assert soma_lista([1,2,3]) == 6
#   assert soma_lista([10,20,30]) == 60
#   print('soma_lista:Todos os testes passaram')


# if __name__=='__main__':
#   test_soma_lista()
  