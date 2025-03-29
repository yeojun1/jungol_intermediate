N=int(input())
a=list(map(int,input().split()))
Q=int(input())
b=list(map(int,input().split()))

def binarySearch(A,low,high,target):
    if low>high: return -1
    
    mid=(low+high)//2
    if A[mid]==target: return mid

    if A[mid]<target: return binarySearch(A,mid+1,high,target)
    return binarySearch(A,low,mid-1,target)

for i in range(Q):
    print(binarySearch(a,0,N,b[i]),end=' ')

