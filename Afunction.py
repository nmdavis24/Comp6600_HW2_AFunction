from math import hypot
current = [[2,3,7,4,5] 
               ,[1,-2,11,-2,8]
               ,[6, 10, -1, 12, 15]
               ,[9,-2, 14,-2, 20]
               ,[13,16,17,18,19]
               ]
    
goal = [[1,2,3,4,5]
        ,[6,-2,7,-2, 8]
        ,[9,10,-1,11,12]
        ,[13,-2,14,-2,15]
        ,[16,17,18,19,20]        
        ]

def A():
    whiteX = 2
    whiteY = 2
    count = 0    
    while True:
        print("Step: " + str(count) + "\n" + str(current))
        if current == goal:
            print("Operation complete. Steps taken: " + str(count))
            return
        # get valid blocks adjacent to whitespace
        adj = []
        if (whiteY != 0 and current[whiteY - 1][whiteX] != -2):
            adj.append(Block(whiteX, whiteY - 1, current[whiteY-1][whiteX]))
        if (whiteY != 4 and current[whiteY + 1][whiteX] != -2):
            adj.append(Block(whiteX, whiteY + 1, current[whiteY+1][whiteX]))
        if (whiteX != 0 and current[whiteY][whiteX - 1] != -2):
            adj.append(Block(whiteX - 1, whiteY, current[whiteY][whiteX - 1]))
        if (whiteX != 4 and current[whiteY][whiteX + 1] != -2):
            adj.append(Block(whiteX + 1, whiteY, current[whiteY][whiteX + 1]))
        # get block with largest manhattan value
        largest = adj[0]
        for i in range(len(adj)):
            if (adj[i].manhat > largest.manhat):
                largest = adj[i]
                
        # switch block w largest h value with whitespace
        current[largest.y][largest.x] = -1
        current[whiteY][whiteX] = largest.num
        whiteX = largest.x
        whiteY = largest.y
        count = count + 1
        
# heuristic function: farthest block from goal gets largest h(x)         
def Manhat(block, x, y):
    goalX = -1
    goalY = -1
    for i in range(5):
        for j in range(5):
            if goal[i][j] == block:
                goalX = j
                goalY = i
                break
    return abs(hypot(x - goalX, y - goalY))

class Block: 
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.manhat = Manhat(num, x, y)
        
A();
        
    