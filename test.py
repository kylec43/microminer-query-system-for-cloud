def a_lessthan_b(a, b):

	least_len = 0

	if len(a) < len(b):
		least_len = len(a)
	else:
		least_len = len(b)

	for i in range(least_len):

		if a[i].upper() == b[i].upper():

			if a[i] == a[i].lower() and b[i] == b[i].upper():
				return True

			elif a[i] == a[i].upper() and b[i] == b[i].lower():
				return False

		else:

			if a[i].upper() <= b[i].upper():
				return True

			else:
				return False

	return True





lis = ["catMan and robin", "Batman and rObin", "Catman and roBin", "batman and robin", "baTman anD roBin"]
lis2 = ["a", "c", "d", "b"]

for i in range(0, len(lis)-1, 1):
	for k in range(0, len(lis)-i-1, 1):

		if not a_lessthan_b(lis[k], lis[k+1]):
			lis[k], lis[k+1] = lis[k+1], lis[k]


print(lis)


