"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


nums = [2,3,4,6,4]
dict_nums = {}

for i in nums:
    if i not in dict_nums.keys():
	dict_nums[i] = 1
    else:
	return(True)
return(False)



#https://www.youtube.com/watch?v=3OamzN90kPg
