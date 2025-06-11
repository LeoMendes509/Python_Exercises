# Solicitação dos dados do usuário

nome = input(' Digite seu nome : ')
idade = input(' Digite sua idade : ')
altura = float(input(' Digite sua altura : '))
peso_Kg_ = float(input(' Digite seu peso em Kg : '))

# Código do cálculo do imc

imc = peso_Kg_ / (altura ** 2)

#CLASSIFICAÇÃO DO IMC

if imc < 16 : 
    classificacao = "Magreza grau 3"
elif 16 <= imc < 16.9 : 
    classificacao = "Magreza grau 2"
elif 17 <= imc < 18.4 : 
    classificacao = "Magreza grau 1"    
elif 18.5 <= imc < 24.9 :
    classificacao = " Eutrofia (Normalidade) "
elif 25 <= imc < 29.9 :
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9 :
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9 :
    classificacao = "Obesidade grau 2"
elif imc < 40 :
    classificacao = "Obesidade grau 3"                

# Exibição dos dados

print('nome:' , nome)
print('idade:',idade)
print('altura:',altura)
print('peso em Kg:',peso_Kg_)
print('imc:' , imc)
print('classificacao:' , classificacao)