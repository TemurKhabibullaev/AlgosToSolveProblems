# Temur Khabibullaev
# Problem: return an index of the first nonrepeating character in the string

def firstNonRepeatingCharacter(string):
    # Write your code here.
	dic = {}
	for i in string:
		if i not in dic:
			dic[i] = 0
		dic[i] += 1
	for a in range(len(string)):
		char = string[a]
		if dic[char] == 1:
			return a
    return -1
