
num = 0
with open("input/input3.txt") as f:
    for line in [x.strip() for x in f.readlines()]:
        [x, y, z] = sorted(map(int,line.split()))
        if x + y > z: num+=1

    print(num)
