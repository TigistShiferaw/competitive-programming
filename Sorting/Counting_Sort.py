def countingSort(arr):
    # Write your code here
    countarr=[0]*(100)
    for i in range(len(arr)):
            countarr[arr[i]]=countarr[arr[i]]+1
    return countarr
