
def third_largest(nums):
	s = sorted(set(nums))
	if len(s) < 3:
		raise ValueError("Array must contain at least three distinct numbers")
	return s[-3]

# MSSQL equivalent to find the third largest distinct number from a table named Numbers
# with a numeric column named value:
#
# SELECT TOP 1 value
# FROM (
#   SELECT DISTINCT TOP 3 value
#   FROM Numbers
#   ORDER BY value DESC
# ) AS top_three
# ORDER BY value ASC;

if __name__ == '__main__':
	arr = [1, 2, 4, 5, 3]
	print(third_largest(arr))
