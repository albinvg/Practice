"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range (len(nums)): 

            if nums[pointer] == 0:                
                nums.append(nums.pop(pointer))
            else:
                pointer +=1
                
                
#============================================
#alternate solution
#https://www.youtube.com/watch?v=aayNRwUN3Do
  
l = 0  ## keep track of 0
for r in range (len(list1)):  #keep track of non-0
  #if non-0 then increase both l/r. 
  #if 0 then only increase r
  if list1[r] != 0:
    list1[l], list1[r] = list1[r], list1[l]
    l +=1
