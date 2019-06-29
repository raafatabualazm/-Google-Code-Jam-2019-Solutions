n = input()
n = int(n)
cases = n
num = 0
num2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n > 0:
    num2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num = input()
    num.split()
    i = len(num) - 1
    num_len = len(num)
    while i >= 0:
        num3[10 - num_len + i] = int(num[i])
        i -= 1
    j = len(num3) - 1
    while j >= 0:
        if num3[j] == 4:
            num3[j] = 2
            num2[j] = 2
        j -= 1

    numout = 1e9*num3[0] + 1e8*num3[1] + 1e7*num3[2] + 1e6*num3[3] + 1e5*num3[4] + 1e4*num3[5] + 1e3*num3[6] + 1e2*num3[7] + 10*num3[8] + num3[9]
    numout2 = 1e9 * num2[0] + 1e8 * num2[1] + 1e7 * num2[2] + 1e6 * num2[3] + 1e5 * num2[4] + 1e4 * num2[5] + 1e3 * num2[6] + 1e2 * num2[7] + 10 * num2[8] + num2[9]
    print('Case #'+ str(cases - n + 1) + ':', int(numout), int(numout2))
    n -= 1