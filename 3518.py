N=int(input())
a=list(map(int, input().split()))

def quickSort(A,low,high):
    pivot=N-1
    while True:
        while A[low]>=A[pivot]: low+=1
        while A[high]<=A[pivot]: high-=1
        A[high],A[low]=A[low],A[high]
        if low>=high:
            print(*A)
            break
    
    if high-low<1:
        A[high],A[pivot]=A[low],A[pivot]
        return
    else:
        mid=int(N/2)
        quickSort(A,0,mid)
        quickSort(A,mid+1, N-1)

quickSort(a,0, N-1)
