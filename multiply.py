def Multiply(M,n):
    if n==1:
        return M
    else :
        return M+Multiply(M,n-1)

M = int(input('Enter value M:'))
n = int(input('Enter value n:'))



while(n!=-1):
    print(Multiply(M,n))
    M = int(input('Enter value M:'))
    n = int(input('Enter value n:'))
