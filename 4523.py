N=int(input())
arr=list(map(int,input().split()))
s,e=map(int,input().split())

part=sorted(arr[s:e+1])
for i in range(0,len(part)):
    arr[i+s]=part[i]

print(*arr)
print(*sorted(arr))