lst=[]
n=int (input("Enter Numbers of Elements:"))
print("Enter Numbers:")
for l in range(0,n):
    ele=int(input())
    lst.append(ele) #adding elements to array

print(lst)
#implement bubblesort
def bubblesort(arr):
    n=len(arr)
    for i in range(1, n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]

 #call to bubblesort
bubblesort(lst)
print("sorted array is :")
print(lst)
