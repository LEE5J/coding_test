N,K = map(int,input().split())
arr = list(map(int,input().split()))

change = 0

for j in range(N-1,0,-1):
    flag=True
    for i in range(0,j):
        if arr[i]>arr[i+1]:
            flag=False
            change+=1
            arr[i],arr[i+1]=arr[i+1],arr[i]
            if change == K:
                print(arr[i],arr[i+1])
                exit()
    if flag:
        break
print(-1)
