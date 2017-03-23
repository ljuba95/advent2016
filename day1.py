
input = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"
position = (0,0)
moves = [(0,1), (1,0), (0,-1), (-1,0)]
direction = 0
locs = set()
first = []

def nextDir(direc):
    return (direction + 1 if direction < 3 else 0) if direc == "R" else (direction - 1 if direction > 0 else 3)

def move(pos,direction):
    return (pos[0] + moves[direction][0],pos[1] + moves[direction][1])

for x in input.split(", "):
    direction = nextDir(x[0])
    for i in range(int(x[1:])):
        position = move(position,direction)
        if position in locs:
            first.append(position)
        else:
            locs.add(position)


print(abs(first[0][0]) + abs(first[0][1]))
