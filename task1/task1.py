import sys
for i in range(1,len(sys.argv),2):
    arg1=sys.argv[i]
    arg2=sys.argv[i+1]
    n = int(''.join(map(str, arg1)))
    m = int(''.join(map(str, arg2)))
    j = 1
    while True:
        print(j, end='')
        j = 1 + (j + m - 2) % n
        if j == 1:
            break
    print()