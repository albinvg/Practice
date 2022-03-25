"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


def searchInsert(self, list1, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(list1) - 1

    while left <= right:
        middle = (left + right) // 2

        if list1[middle] < target:
            left = middle +1
        elif list1[middle] > target:
            right = middle-1
        else:
            return (middle)

    return(left)
