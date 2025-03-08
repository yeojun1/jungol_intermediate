N=int(input())
arr=list(map(int,input().split()))
s,e=map(int,input().split())
filterArr=sorted(list(filter(lambda i: s<=i<=e, arr)))


print(f"{0}\n{sorted(arr)}")