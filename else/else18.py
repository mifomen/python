a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a==b==c:
	print('nothing')
elif a==c:
	print(2)
elif b==a:
	print(3)
elif b==c:
	print(1)
else:
	print('nothing')
