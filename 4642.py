n=int(input())
arr=[]
for i in range(n):
    arr.append(input().split())
    arr[i][1]=int(arr[i][1])

arr.sort(key=lambda x:(-x[1],x[0]))

for j in range(n):
    for k in range(2):
        print(arr[j][k],end=' ')
    print()