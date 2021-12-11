def insertionSort1(n, arr):
    # Write your code here
    current=arr[-1]
    i=len(arr)-2
    while i>=0 and arr[i]>current:
        arr[i+1]=arr[i]
        i-=1
        print(*arr)
    arr[i+1]=current    
    print(*arr)

