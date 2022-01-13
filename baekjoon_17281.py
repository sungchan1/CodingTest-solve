
from itertools import permutations


bestScore = 0 
innings = int(input())
playerCost = list()
for i in range(innings):
    playerCost.append(list(map(int,input().split())))
lotation = list(permutations([1,2,3,4,5,6,7,8],8))
for order in lotation :
    turn = 0 
    score = 0
    for inning in range(innings) :
        field = [0] * 4 
        outcount = 0
        while outcount < 3:
            if turn % 9 == 3 :
                player = 0
            elif turn % 9 > 3  :
                player = order [turn % 9 -1]            
            else : 
                player = order[turn % 9 ]
            situation = playerCost[inning][player]
            if situation == 1:
                if field[2] == 1:
                    field[2] = 0
                    score += 1
                if field[1] == 1:
                    field[1] = 0
                    field[2] = 1
                if field[0] == 1:
                    field[0] = 0
                    field[1] = 1
                field[0] = 1
            elif situation == 2:
                if field[2] == 1:
                    field[2] = 0
                    score += 1
                if field[1] == 1:
                    field[1] = 0
                    score += 1
                if field[0] == 1:
                    field[0] = 0
                    field[2] = 1
                field[1] = 1
            elif situation == 3:
                if field[2] == 1:
                    field[2] = 0
                    score += 1
                if field[1] == 1:
                    field[1] = 0
                    score += 1
                if field[0] == 1:
                    field[0] = 0
                    score += 1
                field[2] = 1
            elif situation == 4:
                if field[2] == 1:
                    field[2] = 0
                    score += 1
                if field[1] == 1:
                    field[1] = 0
                    score += 1
                if field[0] == 1:
                    field[0] = 0
                    score += 1
                score += 1
            elif situation == 0:
                outcount += 1
            else :
                print( "error" ,situation)
            turn += 1
    if score > bestScore:
        bestScore = score
print( bestScore)
                    
                
                
            

