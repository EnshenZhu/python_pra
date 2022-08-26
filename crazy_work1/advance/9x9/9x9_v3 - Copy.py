for a in range(1, 10):
	for b in range(1, a + 1):
		if (a * b) // 10 == 0:
			print(' {}*{}= {} |' .format(a, b, a * b), end='')  # special alignment if the multiplication ouput is one digit
		else:
			print(' {}*{}={} |' .format(a, b, a * b), end='')
	print('')