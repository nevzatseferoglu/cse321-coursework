def binary_to_int(binary_num, i = 0):
    """ convert binary string to integer form """

    length = len(binary_num)

    if (i == length - 1): 
        return int(binary_num[i])

    # shifting make operation constant time
    return ((int(binary_num[i]) << (length - i - 1)) + 
            binary_to_int(binary_num, i + 1))


def q2(arr):
    """ find the absent number in given binary represented array """

    arr_length = len(arr)
    expected_sum = arr_length * (arr_length + 1) / 2
    cur_sum = 0

    for i in arr:
        cur_sum += binary_to_int(i,0)

    return int(expected_sum - cur_sum)


# absent number is '7'
arr = ["00000000",
       "00000001",
       "00000010",
       "00000011",
       "00000100",
       "00000101",
       "00000110",
       "00001000",
       "00001001",
       "00001010",
       "00001011"]


print(q2(arr))