# Temur Khabibullaev
# Find which two values in the list result in targetsum

def twoNumberSum(list, targetSum):
    # Write your code here.
	list.sort()
    left = 0
    right = len(list) - 1
    while left < right:
        possibleSum = list[left] + list[right]
        if possibleSum == targetSum:
            return [list[left], list[right]]
        elif possibleSum < targetSum:
            left += 1
		elif possibleSum > targetSum:
			right -= 1
	return []
