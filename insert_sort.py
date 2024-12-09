length = int(input())

arr = list(map(int, input().split()))
targ_arr = list(map(int, input().split()))

if length == 1:
    if targ_arr[0] == arr[0]:
        print(1)
    else:
        print(0)
    exit()
for i in range(length-1):
    min=arr[i]
    min_idx=i
    # for j in range(i+1,length):
    #     if arr[j]<min:
    #         min = arr[j]
    #         min_idx = j
    # arr[min_idx],arr[i] = arr[i],arr[min_idx]
    min(arr)

    if arr == targ_arr:
        print(1)
        exit()
print(0)