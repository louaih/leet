"""
Louai Hammad
stringtoint.py
Solution to Leetcode #8
"""


def myAtoi(s):
	s = s.strip()
	if not s:
		return 0
	is_neg = s[0] == '-'
	digits = []

	i = 1 if is_neg or s[0] == "+" else 0
	while i < len(s):
		if s[i].isdigit():
			digits.append(s[i])
			i += 1
		else:
			break

	if digits:
		ans = int("".join(digits)) * (-1 if is_neg else 1)
		if is_neg and ans < -2**31:
			return -(2**31)
		elif not is_neg and ans > 2**(31)-1:
			return 2**(31)-1
		else:
			return ans
	else:
		return 0
