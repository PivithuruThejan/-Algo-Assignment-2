import random
def binarySearch (arr, s, e, x):
	if e >= s:
		mid = s + (e - s)/2# creates the mid point
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binarySearch(arr, s, mid-1, x)
		else:
			return binarySearch(arr, mid+1, e, x)
	else:
		return -1


def randomizedbinarySearch (arr, s, e, x):
	if e >= s:
		point = random.randint(s, e)#creates a random point
		if arr[point] == x:
			return mid
		elif arr[point] > x:
			return binarySearch(arr, s, point-1, x)
		else:
			return binarySearch(arr, point+1, e, x)
	else:
		return -1

arr = []
for x in range(10000000):
  arr.append(x)
print(len(arr))
x = -1

result = binarySearch(arr, 0, len(arr)-1, x)

print(result)
