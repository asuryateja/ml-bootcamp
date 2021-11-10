import math
no=int(input())
root=math.sqrt(no)
if int(root+0.5)**2==no:
    print(no,'It is a  perfect number')
else:
    print(no,'It is not a perfect number')