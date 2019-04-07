
N = int(input())
dir = {"E":"S","S":"E"}

for x in range(N):
    size = input()
    lydia = list(input())
    stack = []
    for item in lydia:
        stack.append(dir[item])
    print ("Case #" + str(x+1) + ": " + ''.join([str(x) for x in stack]))