def sortedMerge(a, b, res, n, m):
	i, j, k = 0, 0, 0
	while (i < n):
		res[k] = a[i]
		i += 1
		k += 1
	while (j < m):
		res[k] = b[j]
		j += 1
		k += 1

	res.sort()

a = [ 10, 5, 15 ]
b = [ 20, 3, 2, 12 ]
n = len(a)
m = len(b)
