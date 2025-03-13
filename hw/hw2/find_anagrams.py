"""
Louai Hammad
find_anagrams.py
Solution to Leetcode #438
"""
import collections


def findAnagrams(s, p):
	p_map = collections.Counter(p)
	ans = []
	left = 0
	right = len(p) - 1
	window_map = collections.Counter(s[left:right+1])
	
	while right < len(s):
		if window_map == p_map:
			ans.append(left)
		
		window_map[s[left]] -= 1
		left += 1
		right += 1
		
		if right < len(s):
			window_map[s[right]] += 1

	return ans
