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
