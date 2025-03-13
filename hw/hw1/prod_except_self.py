"""
Louai Hammad
prod_except_self.py
Solution to Leetcode #238
"""


def productExceptSelf(nums):
    n = len(nums)
    answer = [1 for i in range(n)]

    left = 1
    for i in range(n):
        answer[i] *= left
        left *= nums[i]
    
    right = 1
    for i in reversed(range(n)):
        answer[i] *= right
        right *= nums[i]

    return answer
