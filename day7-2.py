def getABAS(string):
    string = list(string)
    for i in range(len(string)-2):
        if string[i] != string[i+1] and string[i] == string[i+2]: yield string[i:i+3]


def isSSL(line):
    parts = line.replace("[", "]").split("]")
    abas = []

    for i in parts[0::2]:
        abas.extend(list(getABAS(i)))

    for aba in abas:
        for b in parts[1::2]:
            if b.find(aba[1] + aba[0] + aba[1]) != -1:
                return True

    return False

with open("input/input7.txt") as f:
    print(sum([isSSL(line) for line in f.readlines()]))
