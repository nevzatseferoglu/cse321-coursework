
# HW5/Q1
# Nevzat Seferoglu
# 171044024

def printPossibleSubsets(arr, i, inSum, pList, table):
        
    if i == 0 and inSum != 0 and table[0][inSum]:
        pList.append(arr[i])
        print(pList)
        pList = []
        return
    
    if i == 0 and inSum == 0:
        print(pList)
        pList = []
        return
    
    if table[i-1][inSum]:
        bList = []
        bList.extend(pList)
        printPossibleSubsets(arr, i-1, inSum, bList, table)

    if inSum >= arr[i] and table[i-1][inSum-arr[i]]:
        pList.append(arr[i])
        printPossibleSubsets(arr, i-1, inSum-arr[i], pList, table)     




def subsetSum(arr, n, inSum):
    if n == 0 or inSum < 0:
        return

    table = [[False for x in range(inSum+1)] for y in range(n)] 
    for i in range(0,n):
        table[i][0] = True
    
    if arr[0] <= inSum:
        table[0][arr[0]] = True
    
    for i in range(1,n):
        for j in range(0,inSum+1):
            if arr[i] <= j:
                table[i][j] = table[i-1][j] or table[i-1][j-arr[i]]
            else:
                table[i][j] = table[i-1][j]

    if table[n-1][inSum] == False:
        print(f"There is no subset with {inSum}")
        return

    pList = []
    printPossibleSubsets(arr, n-1, inSum, pList, table)

if __name__ == "__main__":
     
    arr = [2, 3, -5, -8, 6, -1]
    inSum = 0
    subsetSum(arr, len(arr), inSum)
    