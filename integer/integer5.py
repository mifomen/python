print('Ведите число A')
a=int(input())
print('Ведите число B')
b=int(input())
if a>b : 
	print('Незанятая часть отрезка А', a-b*(a // b)) 
else:
	print('B>A, не могу вычислить')
