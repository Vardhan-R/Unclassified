while True:
    m = int(input("From base "))
    x = str(input("Number: "))
    n = int(input("To base "))
    y = 0
    c = 0
    f = ""
    flist = []

    cA = []
    cB = []
    cC = []
    cD = []
    cE = []
    cF = []
    cG = []
    cH = []
    cI = []
    cJ = []
    cK = []
    cL = []
    cM = []
    cN = []
    cO = []
    cP = []
    cQ = []
    cR = []
    cS = []
    cT = []
    cU = []
    cV = []
    cW = []
    cX = []
    cY = []
    cZ = []


    xlist = []

    for i in x:
        xlist.append(i)

    xlist.reverse()

    for i in xlist:
        if i == "A":
            cA.append(c)
        elif i == "B":
            cB.append(c)
        elif i == "C":
            cC.append(c)
        elif i == "D":
            cD.append(c)
        elif i == "E":
            cE.append(c)
        elif i == "F":
            cF.append(c)
        elif i == "G":
            cG.append(c)
        elif i == "H":
            cH.append(c)
        elif i == "I":
            cI.append(c)
        elif i == "J":
            cJ.append(c)
        elif i == "K":
            cK.append(c)
        elif i == "L":
            cL.append(c)
        elif i == "M":
            cM.append(c)
        elif i == "N":
            cN.append(c)
        elif i == "O":
            cO.append(c)
        elif i == "P":
            cP.append(c)
        elif i == "Q":
            cQ.append(c)
        elif i == "R":
            cR.append(c)
        elif i == "S":
            cS.append(c)
        elif i == "T":
            cT.append(c)
        elif i == "U":
            cU.append(c)
        elif i == "V":
            cV.append(c)
        elif i == "W":
            cW.append(c)
        elif i == "X":
            cX.append(c)
        elif i == "Y":
            cY.append(c)
        elif i == "Z":
            cZ.append(c)

        c = c + 1

    for i in cA:
        xlist[i] = 10
    for i in cB:
        xlist[i] = 11
    for i in cC:
        xlist[i] = 12
    for i in cD:
        xlist[i] = 13
    for i in cE:
        xlist[i] = 14
    for i in cF:
        xlist[i] = 15
    for i in cG:
        xlist[i] = 16
    for i in cH:
        xlist[i] = 17
    for i in cI:
        xlist[i] = 18
    for i in cJ:
        xlist[i] = 19
    for i in cK:
        xlist[i] = 20
    for i in cL:
        xlist[i] = 21
    for i in cM:
        xlist[i] = 22
    for i in cN:
        xlist[i] = 23
    for i in cO:
        xlist[i] = 24
    for i in cP:
        xlist[i] = 25
    for i in cQ:
        xlist[i] = 26
    for i in cR:
        xlist[i] = 27
    for i in cS:
        xlist[i] = 28
    for i in cT:
        xlist[i] = 29
    for i in cU:
        xlist[i] = 30
    for i in cV:
        xlist[i] = 31
    for i in cW:
        xlist[i] = 32
    for i in cX:
        xlist[i] = 33
    for i in cY:
        xlist[i] = 34
    for i in cZ:
        xlist[i] = 35

    for i in range(len(xlist)):
        y = y + (int(xlist[i]) * (m**(int(i))))

    if y < n and n!=10:
        if y in range(0, 10):
            f = y
        elif y == 10:
            f = "A"
        elif y == 11:
            f = "B"
        elif y == 12:
            f = "C"
        elif y == 13:
            f = "D"
        elif y == 14:
            f = "E"
        elif y == 15:
            f = "F"
        elif y == 16:
            f = "G"
        elif y == 17:
            f = "H"
        elif y == 18:
            f = "I"
        elif y == 19:
            f = "J"
        elif y == 20:
            f = "K"
        elif y == 21:
            f = "L"
        elif y == 22:
            f = "M"
        elif y == 23:
            f = "N"
        elif y == 24:
            f = "O"
        elif y == 25:
            f = "P"
        elif y == 26:
            f = "Q"
        elif y == 27:
            f = "R"
        elif y == 28:
            f = "S"
        elif y == 29:
            f = "T"
        elif y == 30:
            f = "U"
        elif y == 31:
            f = "V"
        elif y == 32:
            f = "W"
        elif y == 33:
            f = "X"
        elif y == 34:
            f = "Y"
        elif y == 35:
            f = "Z"

    if y == n and n!=10:
        f = "10"

    if y > n and n!=10:
        while y not in range (0, n):
            r = y%n

            if r in range(0, 10):
                flist.append(r)
            elif r == 10:
                flist.append("A")
            elif r == 11:
                flist.append("B")
            elif r == 12:
                flist.append("C")
            elif r == 13:
                flist.append("D")
            elif r == 14:
                flist.append("E")
            elif r == 15:
                flist.append("F")
            elif r == 16:
                flist.append("G")
            elif r == 17:
                flist.append("H")
            elif r == 18:
                flist.append("I")
            elif r == 19:
                flist.append("J")
            elif r == 20:
                flist.append("K")
            elif r == 21:
                flist.append("L")
            elif r == 22:
                flist.append("M")
            elif r == 23:
                flist.append("N")
            elif r == 24:
                flist.append("O")
            elif r == 25:
                flist.append("P")
            elif r == 26:
                flist.append("Q")
            elif r == 27:
                flist.append("R")
            elif r == 28:
                flist.append("S")
            elif r == 29:
                flist.append("T")
            elif r == 30:
                flist.append("U")
            elif r == 31:
                flist.append("V")
            elif r == 32:
                flist.append("W")
            elif r == 33:
                flist.append("X")
            elif r == 34:
                flist.append("Y")
            elif r == 35:
                flist.append("Z")

            y = y//n

        flist.reverse()
        for i in flist:
            f = f + str(i)
        f = str(y) + f

    if n == 10:
        f = y
    print(f)