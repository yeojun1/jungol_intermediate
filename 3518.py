# https://jeonyeohun.tistory.com/102

N=int(input())
A=list(map(int, input().split()))
print(*A)

def partition(arr:list,p:int,r:int)->int:
    pivot=arr[p]
    low=p+1
    high=r

    while low<high:
        while arr[low]<pivot: low+=1
        while arr[high]>pivot: high-=1
        
        if low<high: arr[low],arr[high]=arr[high],arr[low]
    arr[p],arr[high]=arr[high],arr[p]
    return high

def quickSort(arr,left,right):
    if left<right: pivot=partition(arr,left,right)
    quickSort(arr,left,pivot-1)
    quickSort(arr,pivot+1,right)