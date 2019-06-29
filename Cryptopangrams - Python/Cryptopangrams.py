import math
def primeFactors(n):
    primeList = []
    while n % 2 == 0:
        primeList.append(n)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            primeList.append(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primeList.append(n)

    return primeList


t = int(input())

fact1 = -1
fact2 = -1
cypher = []
decypher = []
lettr_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(t):
    outstr = ""
    inp = input()
    inp = inp.split()
    n = int(inp[0])
    l = int(inp[1])
    b = 0
    prime_set = set()
    letters = dict()
    cypher = []
    decypher = []
    eles = input()
    eles = eles.split()
    for j in range(l):
        el = int(eles[j])
        cypher.append(el)

    #k = 2
    #while k * k <= cypher[0]:
    #    if cypher[0] % k == 0:
    #        fact1 = k
    #        fact2 = int(cypher[0] / k)
    #        break
    #    k += 1
    if cypher[1] % fact1 == 0:
        decypher.append(fact2)
        decypher.append(fact1)
        prime_set.add(decypher[0])
        prime_set.add(decypher[1])
    elif cypher[1] % fact2 == 0:
        decypher.append(fact1)
        decypher.append(fact2)
        prime_set.add(decypher[0])
        prime_set.add(decypher[1])
    for m in range(1, l):
        decypher.append(int(cypher[m] / decypher[m]))
        prime_set.add(decypher[m + 1])
    prime_set = sorted(prime_set)
    for prime in prime_set:
        letters[prime] = lettr_list[b]
        b += 1
    for elem in decypher:
        outstr += letters[elem]
    print('Case #' + str(i + 1) + ': ' + outstr)

