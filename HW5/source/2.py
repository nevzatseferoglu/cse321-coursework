
# HW5/Q2
# Nevzat Seferoglu
# 171044024

def findMinPath(triangle):
    size = len(triangle)
    if size == 1:
        return min(triangle[0])

    table = [[0 for x in range(size)] for y in range(size)]

    endRow = triangle[size - 1]
    for i in range(0,len(endRow)):
        table[size-1][i] = endRow[i]

    for i in range(size-2, -1, -1):
        row = triangle[i]
        for j in range(0, len(row)):
            maxSumLeft = table[i+1][j]
            maxSumRight = table[i+1][j+1]
            currentValue = row[j]
            sumPath = currentValue + min(maxSumLeft, maxSumRight)
            table[i][j] = sumPath

    return table[0][0]

if __name__ == "__main__":
    triangle = [
        [2],
        [5,4],
        [1,4,7],
        [8,6,9,6]]
    print(findMinPath(triangle))