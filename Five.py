def Five(n):
    if n==0 or n==1:
        return n+100
    elif n%5==0:
        return n*Five(n-1)
    else:
        return (n-1)*Five(n-1)

n = int(input('Enter value n:'))

while(n!=-1):
    print(Five(n))
    n = int(input('Enter value n:'))

