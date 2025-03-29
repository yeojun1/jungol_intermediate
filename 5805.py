X, Y = map(int, input().split())
Z = int(100 * Y / X)

def findMinGames(X, Y, Z):
    if X == Y: return -1
   
    # 이분 탐색 범위 설정: 최소값은 1, 최대값은 매우 큰 값(10억)으로 설정합니다.
    left, right = 1, 1000000000
    result = -1
   
    # 이분 탐색 시작 / 범위가 알맞을 때
    while left <= right:
        # 중간값 계산: 추가할 게임 수의 후보
        mid = (left + right) // 2
       
        # 새로운 총 게임 수와 이긴 게임 수를 계산합니다.
        new_x = X + mid
        new_y = Y + mid
        if int(100 * new_y / new_x) > Z:
            # 승률이 증가했을 경우 결과값을 업데이트하고, 탐색 범위를 줄입니다.
            result = mid
            right = mid - 1
        else:
            # 승률이 변하지 않을 경우 탐색 범위를 늘립니다.
            left = mid + 1
    return result

print(findMinGames(X, Y, Z))