"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


list1 = [2,3,4,6,4]
set1 = set()
	
for i in list1:
	if i in set1:
		return True
	else:
		set1.add(i)

return False

#----------------------------------------

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if i == j:
            return True
return False



#https://www.youtube.com/watch?v=3OamzN90kPg
