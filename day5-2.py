import hashlib
CODE = 'cxdnnyjw'

def get_pw(code):
    pw = ['_'] * 8
    i=0
    while '_' in pw[:8]:
        m = hashlib.md5()
        m.update((code + str(i)).encode())
        hashstr = m.hexdigest()
        pos = int(hashstr[5],16)
        if hashstr.startswith("00000") and 0 <= pos < 8 and pw[pos] == '_' :
            pw[pos] = hashstr[6]
        i += 1
    return "".join(pw)

print(get_pw(CODE))