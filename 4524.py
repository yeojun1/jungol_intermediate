_=int(input())
arr=list(map(int,input().split()))
print(*sorted(arr,reverse=True))