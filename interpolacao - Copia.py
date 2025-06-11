# interpolação com strings
nome = 'Leonardo'
idade = 23
variavel = '%s , sua idade é : %.2f anos ' % ( nome , idade)
print(variavel)

# interpolação com números
preco = 49.00
print('O preço do produto é %.2f reais .' % preco)

# inserindo o caracter %
taxa = 15
print('A taxa de imposto é %d%% .' % taxa )

# interpolação com múltiplos valores
produto = 'iphone 15'
quantidade = 3
valor_unitario = 4.800
print(' Você comprou %d unidades de %s por R$%.3f cada.' % ( quantidade , produto , valor_unitario))