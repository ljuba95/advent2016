keypad = ['-------',
          '---1---',
          '--234--',
          '-56789-',
          '--ABC--',
          '---D---',
          '-------']
#pocetak u 5(3,1)
code = ''
x, y = 3, 1
with open("input/input2.txt") as f:
    for line in f.readlines():
        for ch in line:
            if ch == 'U' and keypad[x-1][y] != '-': x -= 1
            if ch == 'D' and keypad[x+1][y] != '-': x += 1
            if ch == 'L' and keypad[x][y-1] != '-': y -= 1
            if ch == 'R' and keypad[x][y+1] != '-': y += 1

        code += keypad[x][y]
print(code)