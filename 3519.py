def mergeSort(A,low,high,B):
    if low>=high:
        return
    mid=(low+high)/2
    mergeSort(A,low,mid,B)
    mergeSort(A,mid+1,high,B)