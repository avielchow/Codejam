#This is time limit exceeded at the moment
#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae

import numpy as np

def histogram_row_count(row, k):
    count = 0
    min = row[0]
    max = min
    for number in row:
        if number < min:
            min = number
        elif number > max:
            max = number

        if max - min > k:
            return count
        else:
            count += 1
    return count

# For each row, define the max length where conditions are met to develop a 'histogram'
def gethistogram(board, k):
    histogram = []
    for row in board:
        histogram.append((histogram_row_count(row,k)))
    return histogram


# Python3 program to find maximum
# rectangular area in linear time
def max_area_histogram(histogram):
    # This function calculates maximum rectangular area under given histogram with n bars

    # Create an empty stack. The stack holds indexes of histogram[] list.
    # The bars stored in the stack are always in increasing order of  their heights.
    stack = []

    max_area = 0  # Initialize max area

    # Run through all bars of given histogram
    index = 0
    while index < len(histogram):

        # If this bar is higher than the bar on top stack, push it to stack

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack, then calculate area of rectangle with
        # stack top as the smallest (or minimum height) bar.'i' is 'right index' for
        # the top and element before top in stack is 'left index'
        else:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with histogram[top_of_stack] stack as smallest bar
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

            # Now pop the remaining bars from
    # stack and calculate area with every popped bar as the smallest bar
    while stack:
        # pop the top
        top_of_stack = stack.pop()

        # Calculate the area with histogram[top_of_stack] stack as smallest bar
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        # update max area, if needed
        max_area = max(max_area, area)

        # Return maximum area under
    # the given histogram
    return max_area

# This code is contributed
# by Jinay Shah

def iterate_circuit_board(circuit_board, C):
    ans = 0
    for x in range(C):
        board = circuit_board[:,x:]
        histogram = gethistogram(board,K)
        max_area = max_area_histogram(histogram)
        if max_area > ans:
            ans = max_area
    return ans

T = int(input())
for test in range(1,T+1):
    R, C, K = [int(x) for x in input().split()]
    circuit_board = []
    for line in range(R):
        circuit_board.append([int(x) for x in input().split()])
    circuit_board = np.array(circuit_board)
    print("Case #" + str(test) + ": " + str(iterate_circuit_board(circuit_board,C)))

