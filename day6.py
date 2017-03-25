
msg1 = ''
msg2 = ''

with open("input/input6.txt") as f:
    for col in zip(*f.readlines()):# * od [[1,2,3],[1,2,3]] odpakuje u listu arg [1,2,3],[1,2,3]
        freq = sorted(list({(col.count(ch),ch) for ch in col}))
        msg1 += freq[-1][1]
        msg2 += freq[0][1]

print(msg1,msg2)