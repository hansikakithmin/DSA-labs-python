lst=[]
n=int (input("Enter Numbers of Elements:"))
print("Enter Numbers:")
for l in range(0,n):
    ele=int(input())
    lst.append(ele) #adding elements to array

print(lst)
#implementation of selection sort
def Selectionsort(A):
    n=len(A)
    for i in range(n):
        min_idx=i
        for j in range(i+1, n):
            if A[min_idx]>A[j]:
                min_idx=j
        #swap the found minimm element with first elelment
        A[i],A[min_idx]=A[min_idx],A[i]

Selectionsort(lst)
print("Sorted arry is :")
print(lst)
