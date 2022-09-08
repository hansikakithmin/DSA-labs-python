lst=[]
n = int(input("Enter Number of Elements:"))
print("Enetr sorted set of numbers:")
for l in range(0,n):
    ele=int(input())
    lst.append(ele)  #adding elements to array

print(lst)
#implementation of bianry search
def BinarySearch(A,min,max,key):
    if max<min:
        return False
    else:
        mid=((min+max)//2)
        if A[mid]>key:
            return BinarySearch(A,mid,mid-1,key)
        elif A[mid]<key:
            return BinarySearch(A,mid+1,max,key)
        else:
            return mid

print("calling to binary search")
answer=BinarySearch(lst,0,len(lst)-1,20)
print("the key found at index",answer)

        
