# Hamming number
import time
start_time = time.time()
import sys
sys.setrecursionlimit(3000)

import itertools

def do_hamming(num ):
    # change this function to a while
    if num == 1:
        return True
    if num % 2 == 0:
        return do_hamming(num / 2 )
    if num % 3 == 0:
        return do_hamming(num / 3 )
    if num % 5 == 0:
        return do_hamming(num / 5 )
    return False

def hamming(hamming_pos, x = 0, pos = 0 ):
    x += 1
    num = do_hamming(x)
    if num:
        pos += 1
        if pos == hamming_pos:
            return x
        else:
            #print (pos, x)
            return hamming(hamming_pos, x, pos )

    

    return hamming(hamming_pos, x, pos )

def assert_equals(input_1, output, error = False):
    global start_time

    print(output)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    if input_1 == output:

        return True
    else:
        return error


print(assert_equals(hamming(19), 32, "hamming(19) should be 32"))
