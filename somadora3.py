# somadora3.py - somadora infinita - versao 3

print 'Digite os valores a somar Seguidos de .'
print 'Para encerrar apenas .'
total = 0
while 1:
	try:
		n = float(raw_input(':'))
		total = total + n
	except:
		break
print 'TOTAL: %s' % total
