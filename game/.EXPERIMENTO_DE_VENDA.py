import math as m
q = 100
p = 1
pf = 10
t = 1
#d = 0

def sigmoid(x):
	return 1 / (1 + m.exp(-x))
	
def qv():
	wp = (p / pf) #porcentagem de p/pf
	wt = t #porcentagem de t/4
	
	
	cp = sigmoid(-wp + 6.5)
	ct = sigmoid(wt - 5.5)
	
	#ERRO NA FORMULA
	return round((cp * q))

for i in range(0, 1):
	print(' qv =', qv() )


