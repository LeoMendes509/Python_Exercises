try:
 horario = float(input('Olá usuário , por favor , que horas são agora ? : '))
 if 0 <= horario < 12:
  print('Bom dia !')
 elif 12 <= horario < 18:
  print('Boa tarde !')
 else :
  print('Boa noite !')
except ValueError :
  print('Digite um horário válido') 