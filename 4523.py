N=int(input())
arr=list(map(int,input().split()))
s,e=map(int,input().split())
a=[]
idx=[]

for i in range(N):
    # 현재 i가 정렬조건을 만족한다면 리스트에 추가
    if s<=arr[i]<=e:
        a.append(arr[i])
        idx.append(i)
a.sort()
idx.sort()

for j in range(len(a)):
    arr[idx[j]]=a[j]


print(*arr)
print(*sorted(arr))