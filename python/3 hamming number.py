# Hamming number
# https://en.wikipedia.org/wiki/Hamming_code
import time
start_time = time.time()

import itertools

def hamming(num):
    num_list = [0] * num

    x2, x3, x5 = 2,3,5

    i, j, k = 0, 0, 0

    for x_num in range(1, num):

        num_list[x_num] = min(x2, x3, x5)

        if x2 == num_list[x_num]:
            i += 1
            x2 = 2 * num_list[i]
        if x3 == num_list[x_num]:
            j += 1
            x3 = 3 * num_list[j]
        if x5 == num_list[x_num]:
            k += 1
            x5 = 5 * num_list[k]
    return num_list[-1]

def assert_equals(input_1, output, error = False):
    global start_time

    print(output)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    if input_1 == output:

        return True
    else:
        return error


print(assert_equals(hamming(357), 182250, "hamming(357) should be 182250"))
