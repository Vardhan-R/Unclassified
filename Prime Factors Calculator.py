while True:
    n=int(input('Natural Number: '))
    l=[2, 3]
    f=''

    for i in range ((l[-1])+2, n+1, 2):
        x=0
        for j in l:
            if ((i%j)!=0):
                x=x+1
            else:
                break

        if (x==(len(l))):
            l.append(i)

    for i in l:
        e=0
        while ((n%i)==0):
            e=e+1
            n=n/i

        x=str(i)
        y=str(e)
        if e!=0 and e!=1:
            f=f+' * '+x+'^'+y
        elif e==1:
            f=f+' * '+x

    print(f[3:])
