# HW5/Q3
# Nevzat Seferoglu
# 171044024


def unboundknapSack(W, weight, value, size):

    table = [[0 for i in range(W+1)]for j in range(len(weight)+1)]

    for i in range(1,len(table)):
        for j in range(1, len(table[0])):
            if weight[i-1] <= j:
                table[i][j] = max(value[i - 1] + table[i][j - weight[i - 1]], table[i - 1][j])
            elif weight[i-1] > j:
                table[i][j] = table[i-1][j]
 
    return table[len(weight)][W]
 
if __name__ == "__main__":

    # 𝑣1= 10, 𝑣2= 4, 𝑣3= 3;
    value = [10, 4, 3]

    # 𝑤1= 5, 𝑤2= 4, 𝑤3= 2;
    weight = [5, 4, 2]

    # capacity
    W = 9

    # size
    size = len(value)

    print(unboundknapSack(W, weight, value, size))