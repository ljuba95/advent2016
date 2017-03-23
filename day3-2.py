num = 0
with open("input/input3.txt") as f:
    lines =  [list(map(int,x.strip().split())) for x in f.readlines()]

    for i in range(0,len(lines) - 2,3):
        for j in range(3):
            x, y , z = sorted([lines[i][j],lines[i+1][j],lines[i+2][j]])
            if(x + y > z): num+=1

    print(num)