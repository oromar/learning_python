def incomodam(n):
  if n <= 0:
    return ''
  if n == 1:
    return 'incomodam'
  else:
    return 'incomodam ' + incomodam(n-1)

def elefantes(n):
  if n <= 0:
    return ''    
  if n == 1:
    return '\nUm elefante incomoda muita gente'
  else:
   return elefantes(n - 1) + '\n' + str(n) + ' elefantes ' + incomodam(n) + ' muito mais' + '\n' + str(n) + ' elefantes incomodam muita gente'

print(elefantes(700))