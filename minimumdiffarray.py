def findMinDiff(arr, n):
	
	diff = 10**20
	for i in range(n-1):
		for j in range(i+1,n):
			if abs(arr[i]-arr[j]) < diff:
				diff = abs(arr[i] - arr[j])
  return diff
arr = [4, 8, 13, 19, 28, 45]
n = len(arr)
print("Minimum difference is " + str(findMinDiff(arr, n)))
