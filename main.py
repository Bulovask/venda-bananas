#Jogo: VENDEDOR DE BANANAS
from game import display, actions, playerdata as pd
import os

while pd.vivo:
	display.show()
	#act = input(' Qual sua ação: ').strip().lower()
	act = input(' O que vai fazer? [dormir, comer, comprar, vender]\n ')
	
	#Testa se tá morto e para o loop se sim
	if not pd.vivo or act == 'exit':
		break
	elif act == '':
		actions.passarMinutos(1)
	elif act == 'dormir':
		actions.dormir()
	elif act in ['comer']:
		actions.comer()
	elif act == 'comprar':
		actions.comprar()
	elif act == 'vender':
		actions.vender()
	else:
		print(' =>"{}" não é uma ação válida'.format(act))
		actions.sleep(0.7)

#Ao sair do while exibe a mensagem de morte
if not pd.vivo:
	print('\n\n [☠]VOCÊ MORREU!!!')
	print(' Você viveu até {}'.format(pd.data))