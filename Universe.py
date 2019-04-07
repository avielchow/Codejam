N = int(raw_input())
    
    
    
def damagedone(prog):
    currentpower = 1
    damage = 0 
    for action in prog:
        if action == 'C':
            currentpower = currentpower * 2
        else:
            damage += currentpower
    return damage
        


for test in range(1,N+1):
    line = raw_input().split()
    shield = int(line[0])
    program = list(line[1])
    damage = damagedone(program)
    print (damage)
    if shield > damage:
        print (0)
    else:
        print(damage - shield)