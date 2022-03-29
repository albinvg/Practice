"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

[1,-2,3,-4,5,6,-7,1]
"""

l = 0
cursum = list1[0]
#maxsum = 0
maxsum =list1[0]

for r in range(len(list1)):
if cursum < 0:
	cursum = 0
	l = r			                          #4

cursum =  sum(list1[l : r+1])	        # 11

if maxsum < cursum:
	maxsum = cursum	                    #11
	listout = list1[l:r+1]	            #[5,6]

  
  
# https://www.youtube.com/watch?v=5WZl3MMT0Eg&feature=youtu.be
