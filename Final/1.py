
def maxlengthPalindrome(givenString):
    size = len(givenString)
    table = [[False] * size for k in range(size)]
    a = 0
    b = 0
    
    for i in range(size):
        table[i][i] = True
        a = i
        b = i

    for i in range(size - 1):
        if givenString[i] == givenString[i + 1]:
            table[i][i + 1] = True
            a = i
            b = i + 1

    for row in range(3, size + 1):
        for col in range(0, size - (row - 1)):
            if givenString[col] == givenString[col + (row - 1)] and table[col + 1][col + (row - 2)]:
                table[col][col + (row - 1)] = True
                a = col
                b = col + (row - 1)

    return givenString[a:b + 1]

if __name__ == '__main__':

    # Ex - 1
    print(maxlengthPalindrome("9876543210123456789"))

    # Ex - 2
    print(maxlengthPalindrome("abcdefeddas"))