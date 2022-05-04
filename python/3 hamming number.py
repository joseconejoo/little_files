# Hamming number
import time
start_time = time.time()

import itertools

def hamming(hamming_pos, x = 0, pos = 0 ):
    while True:
        x += 1

        num = x
        while True:
            if num == 1:
                break
            elif num % 2 == 0:
                num = (num / 2 )
            elif num % 3 == 0:
                num = (num / 3 )
            elif num % 5 == 0:
                num = (num / 5 )

            else:
                break
        if num != 1:
            #print (num, x)
            num = False

        if num:
            #print(pos + 1, x)
            pos += 1
            if pos == hamming_pos:
                #print(x)
                return x
            #else:
                #print (pos, x)
                #return hamming(hamming_pos, x, pos )

    
    #return x
    #return hamming(hamming_pos, x, pos )

def assert_equals(input_1, output, error = False):
    global start_time

    print(output)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    if input_1 == output:

        return True
    else:
        return error


print(assert_equals(hamming(357), 182250, "hamming(357) should be 182250"))
