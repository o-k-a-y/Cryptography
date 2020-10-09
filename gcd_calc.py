def gcd(a, b):
	if a == 0:
		return b
	return gcd(b % a, a)

a = int(input('Please enter a: '))
b = int(input('Please enter b: '))
print(gcd(a, b))