from a_lessthan_b import a_lessthan_b

def partition(lis, low, high):

	last_small = low-1
	pivot = lis[high]

	for i in range(low, high, 1):
		if a_lessthan_b(lis[i], pivot):
			last_small += 1
			lis[i], lis[high] = lis[high], lis[i]

	lis[last_small+1], lis[high] = lis[high], lis[last_small+1]

	return last_small+1



def qs(lis, low, high):
	if low > high:
		return


	part = partition(lis, low, high)
	qs(lis, part+1, high)
	qs(lis, low, part-1)

	