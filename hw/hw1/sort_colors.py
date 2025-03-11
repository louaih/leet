"""
Louai Hammad
sort_colors.py
Solution to Leetcode #75
"""

def sortColors(nums):
	"""
	Do not return anything, modify nums in-place instead.
	"""

	l = 0
	r = len(nums) - 1

	while l <= r:

		if nums[l] == 0:
			l += 1
		else:
			if nums[r] != 0:
				r -= 1
			else: 
				nums[l], nums[r] = nums[r], nums[l]

	r = len(nums) - 1
	while l <= r:

		if nums[l] == 1:
			l += 1
		else:
			if nums[r] != 1:
				r -= 1
			else: 
				nums[l], nums[r] = nums[r], nums[l]
