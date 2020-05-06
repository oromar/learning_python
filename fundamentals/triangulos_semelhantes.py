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

  def semelhantes(self, t):
    l1 = sorted([self.a, self.b, self.c])
    l2 = sorted([t.a, t.b, t.c])
    return l1[0]//l2[0] == l1[1]//l2[1] == l1[2]//l2[2]         

# def testa_retangulo():
#   t = Triangulo(1, 3, 5)
#   assert t.retangulo() == False
#   t = Triangulo(3,4,5)
#   assert t.retangulo() == True
#   print('testa_retangulo: Todos os testes passaram')

# if __name__ == '__main__':
#   testa_retangulo()

def testa_semelhantes():
  t1 = Triangulo(2, 2, 2)
  t2 = Triangulo(4, 4, 4)
  assert t1.semelhantes(t2) == True
  t1 = Triangulo(1, 22, 32)
  t2 = Triangulo(4, 4, 2)
  assert t1.semelhantes(t2) == False
  t1 = Triangulo(6, 6, 6)
  t2 = Triangulo(6, 6, 6)
  assert t1.semelhantes(t2) == True
  print('testa_semelhantes: Todos os testes passaram')

if __name__=='__main__':
  testa_semelhantes()

    

    