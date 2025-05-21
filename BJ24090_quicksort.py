#N, K = map(int,input().split())
#arr = list(map(int,input().split()))
arr = [4,2,1,5,3]
change = 0

def quick_sort(arr):
    if len(arr)==1:
        return arr
    pivot = partition(arr)

def partition(arr):
    global change,K
    pivot = arr[-1]
    i = -1
    for j in range(0,len(arr)-1):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            change +=1
            if change == K:
                print(arr[i],arr[j] if arr[i]<arr[j] else arr[j],arr[i])
        if i+1 != len(arr)-1:
            arr[i+1],arr[-1]=arr[-1],arr[i+1]





