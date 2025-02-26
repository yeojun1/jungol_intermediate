N=int(input())
A=list(map(int, input().split()))

def quickSort(low,high):
    global A,N
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
        quickSort(0,mid)
        quickSort(mid+1, N-1)

quickSort(0, N-1)
