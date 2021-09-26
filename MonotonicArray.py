# Temur Khabibullaev
# In this problem we are to find out if array is monotonic or not.Monotonic- objects from left to right are entirely non-icresing or non-decreasing


def isMonotonic(array):
    # Write your code here.
	dec = True
	inc = True
    if not array or len(array) == 1:
		return True
	track = 0
	while track < len(array) - 1:
		if array[track] > array[track + 1]:
			inc = False
		elif array[track] < array[track + 1]:
			dec = False
		track += 1
	return dec or inc
