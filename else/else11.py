a=int(input())
b=int(input())

if a!=b and a>b:
    a=b=a
elif a!=b and a<b:
    a=b=b
else:
    a=b=0
print('a= ',a ,  'b= ',b)