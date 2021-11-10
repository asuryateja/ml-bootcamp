'''https://colab.research.google.com/drive/1JTzZSN1JwiEXiZ852yI3wfDqyIbcrfzh?usp=sharing'''
def checkpalindrome(n):
	m=n[::-1]
	if m==n:
		return True
	else:
		return False
n=input()

if checkpalindrome(n):
	print("palindrome")
else:
	print("not palindrome")
