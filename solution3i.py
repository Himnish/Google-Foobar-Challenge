def solution(start, length):
    # Your code here
    v1 = start
    v2 = start

    result = 0

    i = 0
    while i < length:
        v1 = v2 + i
        v2 = v1 + length - i - 1
        result ^= xor(v2) ^ xor(v1-1)
        i += 1

    return result


def xor(n):
    if n == 0:
        return 0

    if n & 3 == 0:
        return n
    elif n & 3 == 1:
        return 1
    elif n & 3 == 2:
        return n + 1
    elif n & 3 == 3:
        return 0
