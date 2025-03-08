def mergeSort(A,low,high,B):
    # 리스트 내의 원소가 1개(이하)라면: return
    if low>=high:
        return
    # 분할시키기
    mid=(low+high)//2
    i = low  # 왼쪽 배열의 시작 인덱스
    j = mid + 1  # 오른쪽 배열의 시작 인덱스
    mergeSort(A,low,mid,B)
    mergeSort(A,mid+1,high,B)

    for k in range(low, high + 1):
        if j > high:  # 오른쪽 배열이 다 정렬된 경우
            # 왼쪽 배열 정렬
            B[k] = A[i]
            i += 1
        elif i > mid:  # 왼쪽 배열이 다 정렬된 경우
            # 오른쪽 배열 정렬
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:  # 왼쪽 요소가 오른쪽 요소보다 작거나 같을 경우
            B[k] = A[i]
            i += 1
        else:  # 오른쪽 요소가 왼쪽 요소보다 작을 경우
            B[k] = A[j]
            j += 1
    
    for m in range(low,high+1):
        A[m]=B[m]
    
    print(*A)

N=int(input())
arr=list(map(int,input().split()))

mergeSort(arr,0,N-1,[0]*N)