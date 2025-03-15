def quicksort(a, low, high):
    if low < high:
        # 피벗 값 설정 (현재 배열의 마지막 요소를 피벗으로 사용)
        pivot = a[high]
       
        # i는 피벗보다 작은 값의 인덱스를 추적
        i = low - 1
       
        # low부터 high-1까지 배열을 순회하면서 피벗보다 작은 값은 i의 위치와 교환
        for j in range(low, high):
            if a[j] < pivot:
                # 피벗보다 작은 값을 만났을 때 i를 증가시키고 해당 값을 i와 교환
                i += 1
                a[i], a[j] = a[j], a[i]

        # 피벗을 적절한 위치에 배치 (i+1 자리에 피벗을 넣음)
        i += 1
        a[i], a[high] = a[high], a[i]

        # 현재 배열 상태 출력 (배열을 하나의 줄로 출력)
        for num in a:
            print(num, end=" ")
        print()

        # 피벗의 왼쪽 부분과 오른쪽 부분을 각각 재귀적으로 정렬
        quicksort(a, low, i - 1)  # 피벗의 왼쪽
        quicksort(a, i + 1, high)  # 피벗의 오른쪽

# 사용자로부터 입력 받기
n = int(input())  # 배열의 크기 입력
nums = list(map(int, input().split()))  # 공백으로 구분된 정수 입력

quicksort(nums, 0, n - 1)