def sumcube(n):
    if n == 1:
        return 1
    else :
        return sumcube(n-1)+n*n*n

n = int(input('Enter value n :'))

while(n!=-1):
    print(sumcube(n))
    n = int(input('Enter value n:'))
