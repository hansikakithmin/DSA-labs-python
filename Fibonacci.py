def Fibonacci(n):
    if n<=1:
        return n
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input('Enter value n:'))

while(n!=-1):
    print(Fibonacci(n))
    n = int(input('Enter value n:'))
