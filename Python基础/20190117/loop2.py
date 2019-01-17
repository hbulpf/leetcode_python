n = 201
pow = 1
while n > 0:
	n = n - 1
	if n % 5 == 0:
		continue
	pow = pow * n
print(pow)