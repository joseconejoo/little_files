import time
import copy

start_time = time.time()
original = []
def little_print():
    global puzzle
    for x in range( len( puzzle ) ):
        print(puzzle[x])

def next_zero(puzzle):
    len_puzzle = len(puzzle)

    for y in range(len_puzzle):
        for x in range(len_puzzle):
            if puzzle[y][x] == 0:
                return [y, x]
    return [-1, -1]
def unable_fun(pos_y, pos_x):
    unable = []

    number_len = len (puzzle)
    unable_append = unable.append

    #check columns and rows
    for y in range(number_len):
        if y == pos_y:
            for x in range( number_len ):
                x = puzzle[y][x]
                if (x != 0) and (not (x in unable) ) :
                    unable_append(x)
                    #unable[y] = 1
        
        p_y = puzzle[y][pos_x]
        if (p_y != 0) and (not (p_y in unable)) :
            unable_append(p_y)
        
        y += 1

    # check 3 x 3    
    x3_block_y_start = pos_y - (pos_y % 3)
    x3_block_y_end = x3_block_y_start + 3

    x3_block_x_start = pos_x - (pos_x % 3)
    x3_block_x_end = x3_block_x_start + 3

    for y in range(x3_block_y_start, x3_block_y_end):
        for x in range(x3_block_x_start, x3_block_x_end ):
            elem = puzzle[y][x]
            if (elem != 0) and (not (elem in unable) ) :
                unable_append(elem)
            

    return unable

def point_square(puzzle, pos_x, pos_y):
    len_puzzle = len(puzzle)

    y_next, x_next = next_zero(puzzle)
    if x_next == -1:
        return True

    #print(x_next, y_next, 'next_zero')
    unable_list = unable_fun(y_next, x_next)
    
    if len(unable_list) == 9:
        return False
    for number in range(1, len_puzzle + 1):
        if not (number in unable_list):
            #save y and x 
            puzzle[y_next][x_next] = number
            if point_square(puzzle, x_next, y_next):
                return True
            else:
                puzzle[y_next][x_next] = 0
                #print(x_next, y_next, 'fail')
                if number == 9:
                    return False
        if number == 9:
            return False
                

    return True

def sudoku(puzzle):
    little_print()
    """return the solved puzzle as a 2d array of 9 x 9"""
    #print(puzzle)

    point_square(puzzle, 0, 0)

    return puzzle



puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]


def assert_equals(input_1, output, error = None):
    global start_time

    #print(input_1)
    print("--- %s seconds ---" % (time.time() - start_time))
    little_print()
    if input_1 == output:

        return True
    else:
        #print (error)
        return False
assert_equals(sudoku(puzzle), solution, "Incorrect solution for the following puzzle: " + str(puzzle));
