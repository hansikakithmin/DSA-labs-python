#function
def function(n):
    if n ==1:
        return 1
    else:
        return function(n-1)+n
    
#read input
n = int(input('Enter number:'))

#terminarion loop
while(n!=-1):
    print(function(n))
    n = int(input('Enter number:'))
