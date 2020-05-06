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

  def retangulo(self):
    hipotenusa = self.a
    catetos = [self.b, self.c]
    if self.b > hipotenusa:
      hipotenusa = self.b
      catetos = [self.a, self.c]
    if self.c > hipotenusa:
      hipotenusa = self.c
      catetos = [self.a, self.b]
    return hipotenusa ** 2 == (catetos[0] ** 2) + (catetos[1] ** 2)

# def testa_retangulo():
#   t = Triangulo(1, 3, 5)
#   assert t.retangulo() == False
#   t = Triangulo(3,4,5)
#   assert t.retangulo() == True
#   print('testa_retangulo: Todos os testes passaram')

# if __name__ == '__main__':
#   testa_retangulo()



    

    