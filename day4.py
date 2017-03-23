import re
from collections import defaultdict

res = 0
alpha = "abcdefghijklmnopqrstuvwxyz"
pt2 = 0
def decode(word,num):
    return "".join([" " if ch == "-" else alpha[(alpha.index(ch) + num) % len(alpha)]for ch in word]) #mad

with open("input/input4.txt") as f:
    for line in f.readlines():
        name, sect_id, checksum = re.match('([a-z-]*)-([0-9]*)\\[([a-z]*)\\]', line).groups()
        sect_id = int(sect_id)

        count = defaultdict(lambda : 0)
        for l in re.findall("[a-z]",name):
            count[l] += 1
        count = sorted(count,key = lambda x: (-count[x],x))# sort po broju pa slovu
        #pt 1
        if "".join(count)[:5] == checksum: res+= sect_id

        #pt 2
        if decode(name,sect_id) == 'northpole object storage': pt2 = sect_id #lol

    print(pt2)
    print(decode("x--yz",3))

