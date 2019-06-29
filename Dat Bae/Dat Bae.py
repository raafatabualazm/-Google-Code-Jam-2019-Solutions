import random
t = int(input())
while t > 0:
    broken = []
    inp = input()
    inp = inp.split()
    n = int(inp[0])
    b = int(inp[1])
    f = int(inp[2])
    l = n
    h = 1
    while f > 0 and l > 1:
        broken = []
        broken2 = []
        strout = ""
        l = int(l / 2)
        for j in range(h):
            for i in range(l):
                strout += "1"
            for i in range(l + n % 2):
                strout += "0"
        print(strout, flush=True)
        response = input()
        v = 0
        w = 0
        while v < len(strout) and w < len(response):
            if strout[v] == response[w]:
                v += 1
                w += 1
            elif strout[v] != response[w]:
                broken.append(v)
                v += 1
        v = len(strout) - 1
        w = len(response) - 1
        while v >= 0 and w >= 0:
            if strout[v] == response[w]:
                v -= 1
                w -= 1
            elif strout[v] != response[w]:
                broken2.append(v)
                v -= 1

        h *= 2
        f -= 1
    t -= 1
