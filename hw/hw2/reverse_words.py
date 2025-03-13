"""
Louai Hammad
reverse_words.py
Solution to Leetcode #151
"""


def reverseWords(s):
	return " ".join(reversed(s.strip().split()))
