# f = open('input.txt')
# T = int(f.readline())
# N = number of instructions
# R = number of total rows
# C = number of total columns
# SR = Starting Row
# SC = Starting Column

def go_forward_one(direction, CR, CC):
    if direction == "N":
        CR -= 1
    elif direction == "S":
        CR += 1
    elif direction == "E":
        CC += 1
    elif direction == "W":
        CC -=1
    return CR, CC

def make_move(direction, CR, CC):
    # Move forward to the next square
    CR, CC = go_forward_one(direction, CR, CC)
    # If this square has been visited, go to the next square. While next square is visited, repeat
    while (CR,CC) in visited_squares:
        CR,CC = go_forward_one(direction, CR, CC)
    # append the new square to the visited squares
    visited_squares.append((CR,CC))
    # return the new current location
    return CR, CC

T = int(input())
for test in range(1,T+1):
    N, R, C, SR, SC = [int(x) for x in input().split()]
    directions = input()
    visited_squares = [(SR, SC)]
    current_row = SR
    current_column = SC

    for direction in directions:
        current_row, current_column = make_move(direction, current_row, current_column)
    print("Case #" + str(test) + ": " + str(current_row) + ' ' + str(current_column))


'''
for test in range(1,T+1):
    N, R, C, SR, SC = [int(x) for x in f.readline().split()]
    directions = f.readline().rstrip()

    visited_squares = [(SR,SC)]
    current_row = SR
    current_column = SC

    for direction in directions:
        current_row, current_column = make_move(direction,current_row,current_column)
    print(current_row, current_column)
'''


'''
T = int(input())
for test in range(1,T+1):
    line = input().split()
    N = int(line[0])
    P = int(line[1])
    S = [int(x) for x in input().split()]
    print ("Case #" + str(test) + ": " + str(selectteam(N,P,S)))  
'''