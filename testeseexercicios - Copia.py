def verificar_par_ou_impar(numero):
 return 'par' if numero % 2 == 0 else 'ímpar'

numero = int(input('Digite um número : '))
resultado = verificar_par_ou_impar(numero)
print(f'O número {numero} é {resultado}')