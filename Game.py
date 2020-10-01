def a():
    b = int(input('ENTER THE SIZE OF ARRAY:'))
    c = list(map(int, input('ENTER THE ELEMENTS:').split()))[:b]
    d = [1]*b
    for i in range(b-1):
        p = 1
        m = 0
        j = i+1
        if c[i]<0:
            p = -1
        while j<b:
            if p == -1 and c[j]<0 or p == 1 and c[j]>0:
                break
            p = p * (-1)
            m = m + 1
            j = j + 1
        d[i] = d[i]+m
    for k in d:
        print(k,end=' ')
    print(' ')


a()



def b():
    a = int(input("ENTER NUMBER OF MOVIES:"))
    l = list()
    r = list()
    k = list()
    n = list()
    p = list()
    for i in range(1,a+1):
        d = int(input(f'L{i}:'))
        l.append(d)
        e = int(input(f'R{i}:'))
        r.append(e)
        k.append(d*e)
    lar = max(k)
    for m in range(a):
        if lar == k[m]:
            n.append(m)
    if len(n) == 1:
            if n == 0:
                print('1st MOVIE')
            elif n == 1:
                print('2nd MOVIE')
            elif n == 2:
                print('3rd MOVIE')
            else:
                o = n[0]
                print(f'{o+1}th MOVIE')

    else:
        for j in n:
            p.append(r[j])
        x = max(p)
        for y in range(a):
            if x == r[y]:
                if y == 0:
                    print('1st MOVIE')
                    break
                elif y == 1:
                    print('2nd MOVIE')
                    break
                elif y == 2:
                    print('3rd MOVIE')
                    break
                else:
                    print(f'{y+1}th MOVIE')
                    break


b()


def c():
    a = int(input('SIZE OF ARRAYS:'))
    b = list(map(int, input('ENTER THE ELEMENTS:').split()))[:a]
    d = list()
    s = 0
    for j in '*' * (a - 1):
        i = a - 1
        if b[i] >= b[i - 1]:
            d.append(b[i-1])
            b.pop(i)


        else:
            t = b[i - 1]
            b[i - 1] = b[i]
            b[i] = t
            d.append(b[i-1])
            b.pop(i)
        a = a - 1
    for l in range(len(d)):
        s = s+d[l]
    print(f'OUTPUT:{s}')


c()




