try:
 numero = int(input('Digite um número inteiro : '))
 if numero % 2 == 0 :
  print(f'O número {numero} digitado é par')
 else :
  print(f'O número {numero} digitado é ímpar')
except ValueError:
  print('Por favor , digite um número válido')