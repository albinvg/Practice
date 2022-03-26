"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

#list1 = [1,2,3,0,0,3,4,0,3,0]
list1 = [2,3,4]
target = 6
r = 1
for l in range(len(list1)-1):
	print(l,r, len(list1))
	while ((list1[l] + list1[r]) <= target) and (r < len(list1)):
		if  (list1[l] + list1[r]) == target:
			print (l,r)
			break
		else:
			r +=1
	r = l+2
  
  
  
  # alternate solution
  # https://www.youtube.com/watch?v=cQ1Oz4ckceM
