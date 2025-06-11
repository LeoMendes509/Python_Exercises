# Lidando com erro ao digitar texto
#try:
 #   numero = int(input('Digite um número inteiro:'))
  #  print(f'O número que você digitou é:{numero}')
#except ValueError:
 #   print('Erro : você não digitou um número válido')    

#divisão por 0
#try:
 #   dividendo = int(input('Digite o dividendo:'))
 #   divisor = int(input('Digite o divisor:'))
 #   resultado = dividendo / divisor
  #  print(f'O resultado da divisão é:{resultado}')
#except ZeroDivisionError :
  #  print('Erro : não é posível dividir por zero!')
#except ValueError:
   # print('Erro : você precisa digitar um número válido!')        

# Acesso a um índice inexistente da lista
#try:
  #  lista = [1 , 2 , 3]
  #  indice = int(input('Digite o índice que você quer acessar ( 0, 1 ou 2):'))
  #  print(f'O valor no índice {indice} é {lista[indice]}')
#except IndexError:
  #  print('Erro : Esse índice não existe na lista')
#except ValueError:
  #  print('Você precisa digitar um número inteiro')

# Usando finally para ações finais 
#try:
 #   numero = int(input('Digite um número:'))
 #   print(f'O número digitado foi:{numero}')
#except ValueError:
 #   print("Você digitou algo que não é um número!")
#finally:
 #   print('Fim do programa')
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma é {soma}.")
except ValueError:
    print("Erro: Você precisa digitar números válidos!")