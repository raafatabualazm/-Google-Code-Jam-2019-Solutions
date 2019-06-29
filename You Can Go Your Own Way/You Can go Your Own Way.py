n = int(input())
cases = n
while n > 0:
    size = input()
    path1 = input()
    path2 = ''
    #path1 = path1.split()
    for elem in path1:
        if elem == 'S':
            path2 += 'E'
        elif elem == 'E':
            path2 += 'S'
    print('Case #' + str(cases - n + 1) + ':', path2)
    n -= 1
