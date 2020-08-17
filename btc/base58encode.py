def b58encode(v):
    __b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    __b58base = len(__b58chars)
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * ord(c)
    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result
    nPad = 0
    for c in v:
        if c == '\0': nPad += 1
        else: break
    return (__b58chars[0]*nPad) + result

if __name__ == '__main__':
    print('please input a string:');
    v = input()
    print(b58encode(v))
