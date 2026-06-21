
def third_largest(nums):
	s = sorted(set(nums))
	if len(s) < 3:
		raise ValueError("Array must contain at least three distinct numbers")
	return s[-3]

if __name__ == '__main__':
	arr = [1, 2, 4, 5, 3]
	print(third_largest(arr))
