def binary_Search (array, first, last, target):
    
    if last >= first:
        mid = first + (last - first) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_Search(array, first, mid-1, target) 
        else:
            return binary_Search(array, mid + 1, last, target) 
    else:
        return -1
        
        

        
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 
  
        m = (l+(r-1))//2
  
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
    
def findMultipPairs(array, target):
    
    n = len(array)
    mergeSort(array, 0, len(array) - 1)
    
    for i in range (n) :
        
        x = arr[i]
        mod = target % x
        div = target // x
        
        if mod == 0 :
            searchRes = binary_Search(arr, i+1, n-1, div)
            
            if searchRes != -1 :
                print("(", x, ",", div, ")\n")
                
            
arr = [ 1, 2, 3, 6, 5, 4 ]


findMultipPairs(arr,6)