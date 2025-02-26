N = int(input())
A = list(map(int, input().split()))

def quickSort(low, high):
    global A
    if low >= high:
        return
    
    pivot = A[high]  # 마지막 원소를 피벗으로 설정
    left = low
    right = high - 1 # 피봇 제외

    while left <= right:
        # left와 right가 교차되지 않았을 때 피봇보다 작은 값의 인덱스 구하기
        while left <= right and A[left] < pivot: left += 1
        # " 피봇보다 큰 값의 인덱스 구하기
        while left <= right and A[right] > pivot: right -= 1
        if left <= right: # left와 right가 교차되지 않았을 때 큰 값과 작은 값 바꾸기
            A[left], A[right] = A[right], A[left]
            left += 1 # 바꾼 값 바로 다음 값으로 인덱스 변경
            right -= 1

    # 피벗을 최종적으로 정렬된 위치로 이동
    A[left], A[high] = A[high], A[left]

    print(*A)  # 현재 리스트 상태 출력

    quickSort(low, left - 1)  # 왼쪽 부분 정렬
    quickSort(left + 1, high)  # 오른쪽 부분 정렬

quickSort(0, N - 1)