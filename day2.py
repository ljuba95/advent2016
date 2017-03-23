#x/y0  1  2
#   _  _  _
#0 |1  2  3
#1 |4  5  6
#2 |7  8  9

#3*x + y + 1 yay

code = ''
x, y = 1, 1
with open("input/input2.txt") as f:
    for line in f.readlines():
        for ch in line:
            if ch == 'U' and x > 0: x -= 1
            if ch == 'D' and x < 2: x += 1
            if ch == 'L' and y > 0: y -= 1
            if ch == 'R' and y < 2: y += 1

        code += str(3 * x + y + 1)
print(code)