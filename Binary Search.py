"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""
       
 right = len(nums) -1
  left = 0

  while right != left:

      middle = int((right + left) / 2)

      if target > nums[middle]:
          left = middle+1
      else:
          right = middle

  if nums[left] == target:
      return(left)
  else:
      return (-1)
    
    
    
    
# alternate solution https://www.youtube.com/watch?v=K-RYzDZkzCI
