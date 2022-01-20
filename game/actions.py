#TODAS AS AÇÕES QUE O JOGADOR PODE FAZER
from math import exp
from time import sleep
from random import randint
from perlin_noise import PerlinNoise
import game.playerdata as pd

noise = PerlinNoise(octaves=1)
#Ações do tempo
def passarMinutos(min = 30):
	pd.data += pd.timedelta(minutes = min)
	
	#Adicione Fome, Adicione ou retire sono
	if pd.dormindo:
		pd.sono /= min * 1.1
		pd.fome += 0.005
	else:
		pd.sono += 0.02 * min
		pd.fome += 0.05 * min
		
	#Fome extrema
	if pd.fome > 70:
		pd.vivo = False
	if pd.sono > 34:
		print(' Você adormeceu pois estava muito cansado')
		dormir()

#Ações que o usuário escolhe
def dormir():
	print('\n Você está Dormindo\n')
	pd.dormindo = True
	t = randint(7,9)
	passarMinutos(t * 60)
	sleep(t * 0.05)
	pd.dormindo = False
	print('\n Você acordou!\n')
	sleep(0.2)


def comer():
	if pd.bananas >= 1:
		if pd.fome > 1:
			pd.fome /= 1.1
			pd.bananas -= 1
			print(' Você acaba de comer uma banana')
		else:
			print(' Você não está com fome')
	else:
		print(' Desculpe mais você não tem mais bananas')
	sleep(1)


def comprar():
	if pd.data.weekday() == 6:
		print(' Não vendemos bananas aos domingos')
		passarMinutos(randint(8, 13))
	elif not (18 > pd.data.hour > 5):
		print(' Esta fechado!')
	else:
		limite = int((noise(pd.data.day / 1.2) + 0.5) * 1000)
		pd.preco = float('{:.2f}'.format((noise(pd.data.day / 2.1) + 0.6) * 3))
		
		print(' O preço da banana é R$:{}, temos {} bananas.'.format(pd.preco, limite))
		
		q = input(' Quantidade: ')
		#Valide q
		if q.isnumeric() and int(q) > 0:
			q = int(q)
			
			#peça cconfirmação
			conf = input(' Total a pagar: R$:{:.2f}.\nDigite [1] para confirmar: '.format(q * pd.preco))
			
			#Teste se a compra é possível
			if q > limite:
				print(' Desculpa mais não é possível vender essa quantidade!')
			elif pd.dinheiro > pd.preco * q:
				pd.bananas += q
				pd.dinheiro -= pd.preco * q
				print('\n Compra feita com sucesso!\n')
			elif conf != '1':
				print('\n Compra cancelada!\n')
			else:
				print('\n Dinheiro insuficiente!\n')
			
			#Passe uma hora do relógio
			passarMinutos(randint(20, 40))
		else:
			passarMinutos(randint(10, 30))
			print(' Quantidade invalida!!')
	sleep(1.5)


def vender():
	q = float(input(' Quantas Bananas vai vender? ') or 1)
	
	if 0 < q <= pd.bananas:
		p = float(input(' Preço de cada banana: R$:') or pd.preco)
		h = float(input(' Quantas horas vai ficar vendendo? ') or 1)
		
		if h > 8 and pd.data.hour + h <= 18:
			print(' Não é possível trabalhar mais que oito horas consecutivas')
		elif p > randint(20, 25):
			print(' Esse preço é um absurdo!!!')
			passarMinutos(randint(30,40))
		elif p >= 0.01:
			#Veja se é possivel vender
			def sigmoid(x):
				return 1 / (1 + exp(-x))
			
			#####Inicio######
			##variaveis auxiliares
			cp = sigmoid(-(p / pd.preco) + 6.5)
			ct = sigmoid(h - 5.5)
			
			##Quantidade vendida
			qv = round(cp * ct * q)
			######Fim######
			
			if pd.data.weekday() == 6:
				qv = 0
				print(' Hoje é domingo')
			
			#Setando as propriedades
			pd.bananas -= qv
			pd.dinheiro += qv * p
			
			passarMinutos(h * 60)
			
			print(' Você vendeu {} bananas'.format(qv))
		else:
			print(' O preço precisa ser positivo!')
	else:
		print(' Não é possível vender...')
	sleep(1)

