#This is time limit exceeded at the moment
#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae

from collections import deque
import numpy as np

def get_all_histograms(board):
    histograms = []
    for row in board:
        histogram = []
        start = row[0]
        count = 0
        for number in row:
            if number == start:
                count += 1
            else:
                histogram.append(count)
                for x in reversed(range(1, count)):
                    histogram.append(x)
                start = number
                count = 1
        histogram.append(count)
        for x in reversed(range(1,count)):
            histogram.append(x)
        histograms.append(histogram)

    histograms = np.array(histograms).T.tolist()
    return histograms

# Python3 program to find maximum
# rectangular area in linear time
def largestRectangleArea(heights):
    stack = [-1]
    maxArea = 0

    for i in range(len(heights)):
        # we are saving indexes in stack that is why we comparing last element in stack
        # with current height to check if last element in stack not bigger then
        # current element
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            lastElementIndex = stack.pop()
            maxArea = max(maxArea, heights[lastElementIndex] * (i - stack[-1] - 1))
        stack.append(i)

    # we went through all elements of heights array
    # let's check if we have something left in stack
    while stack[-1] != -1:
        lastElementIndex = stack.pop()
        maxArea = max(maxArea, heights[lastElementIndex] * (len(heights) - stack[-1] - 1))

    return maxArea

def iterate_circuit_board_quick(board):
    ans = 0
    histograms = get_all_histograms(board)
    for histogram in histograms:
        max_area = largestRectangleArea(histogram)
        if max_area > ans:
            ans = max_area
    return ans


T = int(input())
for test in range(1,T+1):
    R, C, K = [int(x) for x in input().split()]
    circuit_board = []
    for line in range(R):
        circuit_board.append(deque([int(x) for x in input().split()]))

    print("Case #" + str(test) + ": " + str(iterate_circuit_board_quick(circuit_board)))
