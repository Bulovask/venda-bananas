from datetime import datetime, timedelta

#DADOS DO JOGADOR
vivo = True
dormindo = False

#1
fome = 0
sono = 0

#2
dinheiro = 20
bananas = 5

#3
data = datetime(1980, 3, 2, 5, 30)
diasDaSemana = [
	'SEG', 'TER', 'QUA', 'QUI',
	'SEX', 'SAB', 'DOM'
]

#DADOS EXTRAS
preco = 1 #Preço dos fornecedores

#Métodos
##1
def getFome():
	texts = [
		'Barriga cheia',
		'Estou com fome',
		'Muita fome!',
		'Estou com MUITA FOME!!!'
	]
	
	#Retorne um texto sobre a fome do jogador
	i = 0
	if fome < 2.5:
		i = 0
	elif fome < 5:
		i = 1
	elif fome < 7.5:
		i = 2
	else:
		i = 3
	return texts[i]

def getSono():
	texts = [
		'Descansado',
		'Um pouco cansado',
		'Cansado',
		'Muito Cansando',
		'Com muito sono'
	]
	
	#Retorne o texto sobre o sono do jogador
	i = 0
	if sono < 2:
		i = 0
	elif sono < 4:
		i = 1
	elif sono < 6:
		i = 2
	elif sono < 8:
		i = 3
	else:
		i = 4
	return texts[i]
	
#2

#3
def getDia():
	i = data.weekday()
	return diasDaSemana[i]