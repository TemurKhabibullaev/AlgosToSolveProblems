# Temur Khabibullaev
# Given unsorted array and a TargetSum is the sum of three values in the list

def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
    tempList = []
	for i in range(len(array)-2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			curSum = array[i] + array[left] + array[right]
			if curSum == targetSum:
				tempList.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif curSum < targetSum:
				left += 1
			elif curSum > targetSum:
            	right -= 1
	return tempList
