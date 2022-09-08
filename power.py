def pov(x,n):
    if n == 0:
        return 1
    else :
        return x*pov(x,n-1)

x = int(input('Enter value x:'))
n = int(input('Enter value n:'))

while(n!=-1):
    print(pov(x,n))
    x = int(input('Enter value x:'))
    n = int(input('Enter value n:'))

