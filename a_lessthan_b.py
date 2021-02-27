def a_lessthan_b(a, b):

	a = a.strip().split(' ')
	b = b.strip().split(' ')

	a = "".join(a)
	b = "".join(b)

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
