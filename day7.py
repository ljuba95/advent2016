
def hasABBA(string):
    string = list(string)
    for i in range(len(string)-3):
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]: return True
    return False


with open("input/input7.txt") as f:
    num = 0
    for line in f.readlines():
        parts = line.replace("[","]").split("]")
        non_brack = False
        brack = False
        for i in parts[1::2]:
            if hasABBA(i):
                brack = True
                break
        if not brack:
            for j in parts[0::2]:
                if hasABBA(j):
                    num += 1
                    break
    print(num)


