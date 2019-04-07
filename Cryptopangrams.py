import string
from collections import deque

Z = int(input())
alphabet = list(string.ascii_uppercase)

def primesall(n):
    sieve = [True] * (n//2)

    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            '''sieve[i*i//2::i]'''
            '''every third i after 4 == false. sieve[4],sieve[7],sieve[10] or 9,15,21 because every other one will be even!'''
            ''' 5*5//2 == 12. 12, 17, 22 etc.''' 
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    
    ''' sieve[1] = represents 3, sieve[2] represents 5, sieve[3] represents 7...'''
    return [2*i+1 for i in range(1,n//2) if sieve[i]]

'''factorization of semi-prime - first number'''

def semiprime1(start,prime):
    primes1 = [x for x in prime if x%10 == 1]
    primes3 = [x for x in prime if x%10 == 3]
    primes7 = [x for x in prime if x%10 == 7]
    primes9 = [x for x in prime if x%10 == 9]
    
    for x in primes9:
        for y in primes9:
            if x*y == start:
                return x,y
            
    for x in primes3:
        for y in primes7:
            if x*y == start:
                return x,x

    for x in primes1:
        for y in primes1:
            if x*y == start:
                return x,y
    
def semiprime3(start,prime):
    primes1 = [x for x in prime if x%10 == 1]
    primes3 = [x for x in prime if x%10 == 3]
    primes7 = [x for x in prime if x%10 == 7]
    primes9 = [x for x in prime if x%10 == 9]    
    
    for x in primes1:
        for y in primes3:
            if x*y == start:
                return x,y
    
    for x in primes7:
        for y in primes9:
            if x*y == start:
                return x,y
    
def semiprime5(start):
    return [5, start//5]
    
def semiprime7(start,prime):
    primes1 = [x for x in prime if x%10 == 1]
    primes3 = [x for x in prime if x%10 == 3]
    primes7 = [x for x in prime if x%10 == 7]
    primes9 = [x for x in prime if x%10 == 9]   
    
    for x in primes7:
        for y in primes1:
            if x*y == start:
                return x,y
    
    for x in primes3:
        for y in primes9:
            if x*y == start:
                return x,y
    
def semiprime9(start,prime):

    primes1 = [x for x in prime if x%10 == 1]
    primes3 = [x for x in prime if x%10 == 3]
    primes7 = [x for x in prime if x%10 == 7]
    primes9 = [x for x in prime if x%10 == 9]
    
    for x in primes7:
        for y in primes7:
            if x*y == start:
                return x,y
        
    for x in primes9:
        for y in primes1:
            if x*y == start:
                return x,y

    for x in primes3:
        for y in primes3:
            if x*y == start:
                return x,y
            
def answer(a,b,code):
    solution = []
    solution.append(a)
    solution.append(b)
    for x in code:
        if x%solution[-1]==0:
            solution.append(x//solution[-1])
        else:
            return "fail"
    return solution

def answer2(a,b,code):
    solution = []
    solution.append(b)
    solution.append(a)
    for x in code:
        solution.append(x//solution[-1])
    return solution
    

'''main'''

for case in range(Z):
    N,L = [int(x) for x in input().split()]
    code = deque([int(x) for x in input().split()])
    prime = primesall(N+1)
    start = code.popleft()
    if start%10 == 1:
        a,b = semiprime1(start,prime)
    elif start%10 == 3:
        a,b = semiprime3(start,prime)
    elif start%10 == 5:
        a,b = semiprime5(start,prime)
    elif start%10 == 7:
        a,b = semiprime7(start,prime)
    elif start%10 == 9:
        a,b = semiprime9(start,prime)
    
    
    temp = answer(a,b,code)
    if temp == "fail":
        result = answer2(a,b,code)
    else:
        result = answer(a,b,code)

    primesinuse = set()
    for x in list(result):
        primesinuse.add(x)
        
    primesinuse = list(primesinuse)
    primesinuse.sort()
    

    cipher = dict(zip(primesinuse,alphabet))
    
    theend = []
    for x in result:
        theend.append(cipher[x])
    print ("Case #" + str(case+1) + ": " + ''.join(theend))
    
        


