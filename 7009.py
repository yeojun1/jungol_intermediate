N,Q=map(int,input().split())
vill=sorted(list(map(int,input().split())))
sus=list(map(int,input().split()))
susNotInVill=[]

def binarySearch(A,low,high,target):
    
    mid=(low+high)//2
    if low>high or mid>=N: return -1
    if A[mid]==target: return mid

    if A[mid]<target: return binarySearch(A,mid+1,high,target)
    return binarySearch(A,low,mid-1,target)

for i in range(Q):
    if binarySearch(vill,0,N,sus[i])!=-1: continue
    susNotInVill.append(sus[i])

if susNotInVill: print(*susNotInVill)
else: print(-1)