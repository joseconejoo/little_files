#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

def print_battlefield(field):
    for row in field:
        print(' '.join(str(cell) for cell in row))

def check_sequence(field, row, col, direction):
    sequence_count = 0
    if direction == 'horizontal':
        while col < len(field[0]) and field[row][col] == 1:
            sequence_count += 1
            col += 1
    elif direction == 'vertical':
        while row < len(field) and field[row][col] == 1:
            sequence_count += 1
            row += 1
    return sequence_count
def replace_sequence(field, row, col, sequence_count, direction):
    last_col = col
    last_row = row
    if direction == 'horizontal':
        for i in range(sequence_count):
            #field[row][col+i] = 'X'
            field[row][col + i] = sequence_count
        last_col = sequence_count
    elif direction == 'vertical':
        for i in range(sequence_count):
            #field[row+i][col] = 'X'
            field[row + i][col] = sequence_count
        last_row = sequence_count
    # Check the corners of the sequence
    corners = [[row-1, col-1], [row-1, col+1], [row+1, col-1], [row+1, col+1]]
    for corner in corners:
        r, c = corner
        if r >= 0 and r < len(field) and c >= 0 and c < len(field[row]) and field[r][c] == 1:
            return False

    return True
def validate_battlefield(original_field):
    field = [row[:] for row in original_field]

    # Check that there are the correct number of ships.
    ship_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    for row in range(len(field)):
        for cell in range(len(field[row])):
            if field[row][cell] == 1:
                result = True
                horizontal_sequence = check_sequence(field, row, cell, 'horizontal')
                vertical_sequence = check_sequence(field, row, cell, 'vertical')
                sequence_count = max(horizontal_sequence, vertical_sequence)
                if horizontal_sequence > vertical_sequence:
                    if vertical_sequence > 1:
                        return False
                    result = replace_sequence(field, row, cell, sequence_count, 'horizontal')
                else:
                    if horizontal_sequence > 1:
                        return False
                    result = replace_sequence(field, row, cell, sequence_count, 'vertical')

                if result == False:
                    return result
                if sequence_count > 4:
                    return False
                ship_counts[sequence_count] += 1
            else:
                field[row][cell] = 'Y'

    if ship_counts != {1: 4, 2: 3, 3: 2, 4: 1}:
        return False
    else:
        return True

def test_validate_battlefield(field_response, must_return, error_message):
    if field_response == must_return:
        return 'Success Test.'
    else:
        return error_message

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleField2 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
battleField3 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#print(test_validate_battlefield(validate_battlefield(battleField),True ,"Nope,Something is wrong!"))
print(test_validate_battlefield(validate_battlefield(battleField3),False ,"Nope,Something is wrong!"))
