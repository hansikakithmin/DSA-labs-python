def sum(n):
    if n ==1:
        return 1
    else:
        return sum(n-1)+n

n = int(input('Enter value n:'))

while(n!=-1):
    print(sum(n))
    n = int(input('Enter value n:'))


        
