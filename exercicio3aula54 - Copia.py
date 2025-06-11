try :
 nome = input('Olá , digite seu nome : ')
 if not nome.isalpha():
   print('Digite um nome válido , apenas letras são permitidas')
 else :  
  tamanho_nome = len(nome)
 if tamanho_nome < 4 :
  print ('Seu nome é muito curto .')
 elif 4 <= tamanho_nome <= 6 :
   print ('Seu nome é normal .')
 else :
   print ('Seu nome é muito grande')
except ValueError :
   print ('Digite um nome válido')