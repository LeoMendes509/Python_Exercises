# Solicitação dos dados do usuário
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = float(input('Digite sua altura em metros (ex: 1.75): '))
peso_kg = float(input('Digite seu peso em kg: '))

# Cálculo do IMC
imc = peso_kg / (altura ** 2)

# Classificação do IMC
if imc < 16:
    classificacao = "Magreza grau 3"
elif 16 <= imc < 17:
    classificacao = "Magreza grau 2"
elif 17 <= imc < 18.5:
    classificacao = "Magreza grau 1"
elif 18.5 <= imc < 25:
    classificacao = "Eutrofia (Normalidade)"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

# Exibição dos dados
print("\n--- Resultado ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso_kg:.2f} kg")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")