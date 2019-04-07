N = int(input())


for line in range(N):
    number = list(input())
    number = [int(x) for x in number]
    number.reverse()
    a = []
    b = []
    for index, digit in enumerate(number):

        if digit == 4:
            a.append(digit - 1)
            b.append(1 * 10**index)
        else:
            a.append(digit)
    a.reverse()
    
    print ("Case #" + str(line+1) + ": " + ''.join([str(x) for x in a]) + " " + str(sum(b)))
