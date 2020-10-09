def is_primitive_root(n, mod):
	primitive_list = []
	k = 1
	for x in range(k, mod):
		num = pow(n, k)
		num = num % mod
		if num not in primitive_list:
			primitive_list.append(num)
		else:
			print(n, "is not a primitive root")
			return False
		k += 1
	print(n, "is a primitive root")
	return True


mod = 11
for i in range(1, mod-1):
	is_primitive_root(i, mod)
