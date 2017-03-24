import hashlib
CODE = 'cxdnnyjw'

def get_pw(code):
    pw = ''
    i = 0
    while len(pw) < 8:
        m = hashlib.md5()
        m.update((code + str(i)).encode())
        hashstr = m.hexdigest()
        if hashstr.startswith("00000"):
            pw += hashstr[5]
        i += 1
    return pw

print(get_pw(CODE))