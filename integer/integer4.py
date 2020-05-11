print('Ведите число A')
a=int(input())
print('Ведите число B')
b=int(input())
if a>b : 
	print('Столько раз B содержится в А', a // b) 
else:
	print('B>A, не могу вычислить')
