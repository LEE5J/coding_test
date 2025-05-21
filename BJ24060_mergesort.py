#clear
chnge = 0
def merge_sort(sub_arr):
    if len(sub_arr)==1:
        return sub_arr
    div = int((len(sub_arr)+1)/2)
    a_arr = merge_sort(sub_arr[:div])
    b_arr = merge_sort(sub_arr[div:])
    return merge(a_arr,b_arr)
def merge(arr0, arr1):
    global chnge
    tmp = list()
    i, j = 0,0
    while len(arr0)>i and len(arr1)>j:
        chnge += 1
        if arr0[i] < arr1[j]:
            tmp.append(arr0[i])
            i+=1
        else:
            tmp.append(arr1[j])
            j+=1
        if chnge == K:
            print(tmp[-1])
    while len(arr0)>i or len(arr1)>j:
        chnge += 1
        if len(arr0) == i:
            tmp.append(arr1[j])
            j+=1
        else:
            tmp.append(arr0[i])
            i+=1
        if chnge == K:
            print(tmp[-1])
    return tmp

# N개의 서로 다른 양의 정수가 저장된 배열 A
N, K  = map(int,input().split())
arr = list(map(int,input().split()))
#N, K = 5,3
#arr = [4,5,1,3,2]
merge_sort(arr)
if chnge < K:
    print(-1)
#print(merge_sort(arr))