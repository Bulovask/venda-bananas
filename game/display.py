import os
import game.playerdata as pd

#MOSTRE AS INFORMAÇÕES NA TELA
def show():
	#limpe a tela
	os.system('clear; clear; clear;')
	
	#Número de colunas
	w = int(os.popen('stty size', 'r').read().split()[1])
	col1 = w // 2
	col2 = w // 2 - 1 if w % 2 == 0 else w // 2
	
	#Defina os objetos da tela
	templateCol = '{0:^{2}}={1:^{3}}'
	
	inv = '{} Bananas'.format(pd.bananas)
	din = 'R$:{:.2f}'.format(pd.dinheiro)
	
	data = pd.data.strftime('{} %d/%m/%Y %Hh:%Mmin'.format(pd.getDia()))
	
	fome = '{0:^{1}}'.format(pd.getFome(), w)
	sono = '{0:^{1}}'.format(pd.getSono(), w)
	
	titulo = '{0:=^{1}}'.format('BANCA DE BANANAS', w)
	corpo = '{0:^{1}}'.format(data, w)
	corpo += templateCol.format(din, inv, col1, col2)
	corpo += '{0:^{2}}{1:^{2}}'.format(fome, sono, w)
	rodape = w * '='
	
	#imprima na tela
	print('{0}{1}{2}'.format(titulo, corpo, rodape))