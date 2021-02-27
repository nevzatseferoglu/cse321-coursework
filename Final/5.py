    
def merge(arrP0, arrP1):
    inversions = 0
    result = []
    while len(arrP0) > 0 and len(arrP1) > 0:
        if arrP0[0] <= arrP1[0]:
            result.append(arrP0.pop(0))
        else:
            if arrP0[0] > 2 * arrP1[0]:
                inversions += len(arrP0)
            result.append(arrP1.pop(0))
      
    if len(arrP0) == 0:
        result += arrP1
    elif len(arrP1) == 0:
        result += arrP0
        
    return result, inversions

def mergeSort(arr):
    length = len(arr)
    mid = length // 2
    if length >= 2:
        sortedP0, countP0 = mergeSort(arr[:mid])
        sortedP1, countP1 = mergeSort(arr[mid:])
        result, counts = merge(sortedP0, sortedP1)
        return result, counts + countP0 + countP1
    else:
        return arr, 0

def numberOfInverison(a):
    resultArray, inversions = mergeSort(a)
    return inversions
      

if __name__ == '__main__':
    arr = [3, 1, 2, 5, 12, 24]
    print(arr)
    print(f"Inversion number: {numberOfInverison(arr)}")
    print('')

    arr = [1,3,12,9,8,13,14,17,6,3]
    print(arr)
    print(f"Inversion number: {numberOfInverison(arr)}")