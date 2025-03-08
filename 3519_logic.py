def mergesort(a, low, high, b):
    if low >= high:  # 배열의 크기가 1 이하이면 정렬할 필요 없음
        return

    mid = (low + high) // 2  # 중간 인덱스 계산

    mergesort(a, low, mid, b)  # 왼쪽 절반 정렬
    mergesort(a, mid + 1, high, b)  # 오른쪽 절반 정렬

    i = low  # 왼쪽 배열의 시작 인덱스
    j = mid + 1  # 오른쪽 배열의 시작 인덱스

    # 두 배열을 합쳐 정렬된 배열 생성
    for k in range(low, high + 1):
        if j > high:  # 오른쪽 배열이 모두 소진된 경우
            b[k] = a[i]
            i += 1
        elif i > mid:  # 왼쪽 배열이 모두 소진된 경우
            b[k] = a[j]
            j += 1
        elif a[i] <= a[j]:  # 왼쪽 요소가 오른쪽 요소보다 작거나 같을 경우
            b[k] = a[i]
            i += 1
        else:  # 오른쪽 요소가 왼쪽 요소보다 작을 경우
            b[k] = a[j]
            j += 1

    # 정렬된 배열을 원본 배열에 복사
    for i in range(low, high + 1):
        a[i] = b[i]

    # 현재 상태의 배열 출력
    for num in a:
        print(num, end=" ")
    print()


# 입력 처리
n = int(input())  # 배열 크기 입력
nums = list(map(int, input().split()))  # 배열 요소 입력

# 병합 정렬 실행
mergesort(nums, 0, n - 1, [0] * n)
