n=int(input());
l=[2, 3];

while ((len(l))<n):
    for i in range ((l[-1])+2, 100, 2):
        x=0;

        for j in l:
            if ((i%j)!=0):
                x=x+1;

            else:
                break;

        if (x==(len(l))):
            l.append(i);

print(l, len(l));
