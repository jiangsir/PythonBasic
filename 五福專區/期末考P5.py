import math
n, a, b= map(int, input().split())
if a-b>0:
	print( math.ceil((n-a)/(a-b))+1 )	
else:
	print('-1')