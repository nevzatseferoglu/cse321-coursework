
def pair(arr, num):
    pairs = []

    arr_set = sorted(set(arr))
    for i in range(len(arr_set)):
        if (num % arr_set[i] == 0):
            temp = binarySearch(arr_set, i, len(arr_set), num // arr_set[i])
            pairs.append( (arr_set[i], arr_set[temp]) ) if (temp != -1) else None
    return pairs 
    

def binarySearch(arr, low, high, item):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] == item:
        return mid
    elif item < arr[mid]:
        return binarySearch(arr, low, mid-1, item)
    else:
        return binarySearch(arr, mid+1, high, item)


arr = [1, 2, 3, 3, 4, 10, 40]
print(pair(arr, 40))
