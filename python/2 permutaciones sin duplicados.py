# permutation solver without duplicates
import time
start_time = time.time()

import itertools
def get_variations(string, pos ):
    len_string = len(string)

    if pos == len_string :
        temp_s = ''.join(string)
        list_perm.append(temp_s)

    for x in range( pos , len_string ):
        string2 = list(string)
        string2[pos], string2[x] = string2[x], string2[pos]

        get_variations(string2, pos + 1 )


def permutations(string2):
    global list_perm

    list_perm = []

    get_variations(string2, 0)
    list_perm = list( dict.fromkeys(list_perm) )
    return (list_perm)



def assert_equals(input_1, output, error = None):
    global start_time
    print(len(output))
    print(output)

    print("--- %s seconds ---" % (time.time() - start_time))
    
    if input_1 == output:

        return True
    else:
        #print (error)
        return False

#print(assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']))
#print(assert_equals(sorted(permutations('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'] ))
print(assert_equals(sorted(permutations('abcd')), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'] ))
