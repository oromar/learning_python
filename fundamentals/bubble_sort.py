def bubble_sort(lista):
  for i in range(len(lista)-1, 0, -1):
    for j in range(i):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
        print(lista)
  return lista
      


# def test_bubble_sort():
#   assert bubble_sort([5, 1, 4, 2]) == [1, 2, 4, 5]
#   print('bubble_sort: Todos os testes passaram')


# if __name__=='__main__':
#   test_bubble_sort()