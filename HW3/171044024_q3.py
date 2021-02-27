import random

def insertionSort(arr):
    swapNumber=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                swapNumber+=1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return swapNumber

def quickSort(arr,low,high):
    total_swap_count=0
    if low < high:
        pi,swap_count = rearrenge(arr,low,high)
        total_swap_count += swap_count
        total_swap_count += quickSort(arr, low, pi-1)
        total_swap_count += quickSort(arr, pi+1, high)
    return total_swap_count

def rearrenge(arr,low,high):
    i = ( low - 1 )
    pivot = arr[high]
    swap_count = 0
    for j in range(low , high):

        if   arr[j] < pivot:

            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
            swap_count += 1


    arr[i + 1],arr[high] = arr[high],arr[i + 1]
    swap_count += 1
    return ( i + 1 ),swap_count

def main():

     quicksortAverageSwapCount = 0
     insertionsortAverageSwapCount = 0
     overAllIterAmount = 100

     # -----------------------------------------
     for i in range(overAllIterAmount):
         arr_1 = []
         arr_2 = []
         elementAmount=10
         for i in range(elementAmount):
             temp_rand = random.randint(0,100)
             arr_1.append(temp_rand)
             arr_2.append(temp_rand)

         totalSwapNumber = quickSort(arr_1, 0, elementAmount - 1) 
         quicksortAverageSwapCount += totalSwapNumber
         print(f"Current number of swapts (quick sort)           : {str(totalSwapNumber)}")

         totalSwapNumber = insertionSort(arr_2)
         insertionsortAverageSwapCount += totalSwapNumber
         print(f"Current number of swapts (insertion sort)       : {str(totalSwapNumber)}")
     
     print("\nAfter testing result:")
     print("---------------------")

     quicksortAverageSwapCount /= overAllIterAmount
     insertionsortAverageSwapCount /= overAllIterAmount
     print(f"Average number of swap in quick sort        : {quicksortAverageSwapCount}")
     print(f"Average number of swap in insertion sort    : {insertionsortAverageSwapCount}")


# test execution area
main()


