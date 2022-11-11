for a in range(1, 10):
	for b in range(1, a + 1):
		if b < a:
			if (a == 3 or a == 4) and (b == 2):    # special alignment when a==3 or a==4, and b==2
				print(' {}*{}={}  |' .format(a, b, a * b), end='')
			else:
				print(' {}*{}={} |' .format(a, b, a * b), end='')
		else:
			print(' {}*{}={}' .format(a, b, a * b))