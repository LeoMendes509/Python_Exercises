# Calculadora simples em Python
print(" Selecione a operação desejada : ")
print("1 - Adição")
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

# Escolha a operação
operacao = input('Digite o número da operação : (1/2/3/4) : ')

# Entrada dos números
num1 = float(input(' Digite o primeiro número : '))
num2 = float(input(' Digite o segundo número : '))

# Realizando o cálculo
if operacao == '1' :
    resultado = num1 + num2
    print(f" O resultado da adição é : {resultado}")
elif operacao == '2' :
    resultado = num1 - num2
    print(f" O resultado da subtração é : {resultado}")
elif operacao == '3' :
    resultado = num1 * num2
    print(f" O resultado da multiplicação é : {resultado}")
elif operacao == '4' :
    if num2 != 0 :
        resultado = num1 / num2    
        print(f" O resultado da divisão é : {resultado}")
    else :
     print(f' O resultado da divisão é : { 0 } ')
else :
    print('Operação inválida !')            