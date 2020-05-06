class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def perimetro(self):
    return self.a + self.b + self.c

  def tipo_lado(self):
    tipo = 'escaleno'
    if self.a == self.b and self.b == self.c:
      tipo = 'equilátero'
    elif self.a == self.b or self.a == self.c or self.c == self.b:
      tipo = 'isóceles'
    return tipo    
    
# def testa_triangulo():
#   t = Triangulo(1, 1 , 1)
#   assert t.a == 1
#   assert t. b == 1
#   assert t.c == 1
#   assert t.perimetro() == 3
#   print('testa_triangulo: Todos os testes passaram')

# if __name__ == '__main__':
#   testa_triangulo()

# def testa_tipo_triangulo():
#   t = Triangulo(4, 4, 4)
#   assert t.tipo_lado() == 'equilátero'
#   t = Triangulo(3,4,5)
#   assert t.tipo_lado() == 'escaleno'
#   t = Triangulo(1,1,2)
#   assert t.tipo_lado() == 'isóceles'
#   t = Triangulo(1,2,2)
#   assert t.tipo_lado() == 'isóceles'
#   t = Triangulo(1,2,1)
#   assert t.tipo_lado() == 'isóceles'
#   print('testa_tipo_lado: Todos os testes passaram')

# if __name__ == '__main__':
#   testa_tipo_triangulo()

  
