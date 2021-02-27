
def rearrange(arr, low, high):

    pivot = arr[high]
    index = low
    i = low

    while i < high:
        if arr[i] <= pivot:
            swap(arr, i, index)
            index += 1
        i += 1

    swap (arr, index, high)
    return index

def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp


def insertionSort(arr, low, high):
    i = low + 1
    while i <= high:
        value = arr[i]
        j = i
        while (j > low and arr[j - 1] > value):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value
        i += 1


def quickSort(arr, low, high):
    while low < high:
        if (high - low ) < 9:
            insertionSort(arr, low, high)
            break
        else:
            pivot = rearrange(arr, low, high)
            if (pivot - low) < (high - pivot):
                quickSort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                quickSort(arr, pivot + 1, high)
                high = pivot - 1


arr = [1, 2, 3, 4, 5, -1, 4, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print(arr)