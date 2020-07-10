a=int(input())
b=int(input())
c=int(input())
if a>0 and b>0 and c>0:
    print(3)
elif (a>0 and b>0) or (b>0 and c>0) or (a>0 and c>0):
    print(2)
elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
    print(1)
else:
    print('0')
