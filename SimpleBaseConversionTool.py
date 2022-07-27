binOctConv = {
"000":"0",
"001":"1",
"010":"2",
"011":"3",
"100":"4",
"101":"5",
"110":"6",
"111":"7"
}

binHexConv = {
"0000":"0",
"0001":"1",
"0010":"2",
"0011":"3",
"0100":"4",
"0101":"5",
"0110":"6",
"0111":"7",
"1000":"8",
"1001":"9",
"1010":"A",
"1011":"B",
"1100":"C",
"1101":"D",
"1110":"E",
"1111":"F"
}


hexConv = {
"A":"10",
"B":"11",
"C":"12",
"D":"13",
"E":"14",
"F":"15",
}

bset = {'1','0'}
fbset = {'1','0','.'}


def hexToOct(a):
    hDigs = {str(i) for i in range(8)}
    hDigs = hDigs.union(set(hexConv.keys()))
    if set(a).issubset(hDigs):
        a = list(a)
        for i in range(len(a)):
            for k in hexConv.keys():
                if a[i] == k:
                    a[i] = hexConv[k]
        a = [int(i) for i in a]
        comps = [8,4,2,1]
        segs = []
        for i in a:
            bins = []
            for c in comps:
                if i-c >= 0:
                    i = i-c
                    bins.append("1")
                else:
                    bins.append("0")
            i = "".join(bins)
            segs.append(i)
            a = "".join(segs)
        threes = []
        while len(a)%3 != 0:
            a = "0"+a
        while len(a) !=0:
            threes.append(a[-3:])
            a = a[:-3]
        threes = threes[::-1]
        threes = [binOctConv[t] for t in threes]
        print("".join(threes))
        return True
    else:
        print("Invalid input provided.")
        return False

def hexToBin(a):
    if "." not in set(a):
        if set(a).issubset(set(binHexConv.values())):
            a = a.upper()
            a = list(a)
            bins = []
            for i in range(len(a)):
                for j in binHexConv.keys():
                    if a[i] == binHexConv[j]:
                        bins.append(j)
            bins = "".join(bins)
            print(bins)
            return True
        else:
            print("Invalid input provided.")
            return False
    else:
        a = a.split(".")
        sides = []
        for i in a:
            i = i.upper()
            i = list(i)
            bins = []
            for k in range(len(i)):
                for j in binHexConv.keys():
                    if i[k] == binHexConv[j]:
                        bins.append(j)
            bins = "".join(bins)
            sides.append(bins)
        sides = ".".join(sides)
        print(sides)
        return True

def octToHex(a):
    bins = []
    if "8" in set(a) or "9" in set(a):
        print("Invalid input provided")
        return False
    elif "." not in a:
        a = list(a)
        for i in a:
            for j in list(binOctConv.keys()):
                if binOctConv[j] == i:
                    bins.append(j)
        bins = "".join(bins)
        while len(bins)%4 != 0:
            bins = "0" + bins
        hexBins = []
        while len(bins) > 0:
            hexBins.insert(0, bins[-4:])
            bins = bins[:-4]
        while hexBins[0] == "0000":
            hexBins = hexBins[1:]
        for i in range(len(hexBins)):
            for j in list(binHexConv.keys()):
                if hexBins[i] == j:
                    hexBins[i] = binHexConv[j]
        hexBins = "".join(hexBins)
        print(hexBins)
        return True

def octToDec(a):
    valSet = list(binOctConv.values())
    valSet.append(".")
    if set(a).issubset(valSet) == False:
        print("Invalid input provided.")
        return False
    elif "." in set(a):
        a = a.split(".")
        a[0] = list(a[0])
        a[0].reverse()
        a[0] = sum([(8**i)*int(a[0][i]) for i in range(len(a[0]))])
        a[1] = list(a[1])
        a[1] = sum([(8**-(1+i))*int(a[1][i]) for i in range(len(list(a[1])))])
        print(sum(a))
        return True
    else:
        a = list(a)
        a.reverse()
        print(sum([(8**i)*int(a[i]) for i in range(len(a))]))
        return True

def octToBin(i):
    cx = []
    valSet = list(binOctConv.values())
    valSet.append(".")
    if set(i).issubset(valSet) == False:
        print("Invalid input provided.")
        return False
    elif "8" in set(i) or "9" in set(i):
        print("Invalid input provided.")
        return False
    elif i in list(binOctConv.values()):
        for k in binOctConv.keys():
            if binOctConv[k] == i:
                print(k)
                return True
    elif "." not in set(i):
        if set(i).issubset(set(binOctConv.values())):
            for a in list(i):
                for k in binOctConv.keys():
                    if binOctConv[k] == a:
                        cx.append(k)
        print("".join(cx))
        return True
    else:
        i = i.split(".")
        i = [list(x) for x in i]
        cy = []
        for j in i:
            cy1 = []
            for k in j:
                for l in binOctConv.keys():
                    if binOctConv[l] == k:
                        cy1.append(l)
            cy1 = "".join(cy1)
            cy.append(cy1)
        print(".".join(cy))
        return True

def binToOct(a):
    if set(a).issubset(bset) and set(a) != fbset:
        nums = []
        while len(a)%3 != 0:
            a = "0" + a
        while len(a) > 0:
            nums.append(a[-3:])
            a = a[:-3]
        nums.reverse()
        b2c = [binOctConv[x] for x in nums]
        print("".join(b2c))
        return True
    elif set(a).issubset(fbset):
        sides = a.split(".")
        for i in range(len(sides)):
            while len(sides[i])%3 != 0:
                sides[i] = "0" + sides[i]
            nums = []
            while len(sides[i]) > 0:
                nums.append(binOctConv[sides[i][-3:]])
                sides[i] = sides[i][:-3]
            sides[i] = "".join(nums)
            nums.reverse()
        sides.reverse()
        sides = ".".join(sides)
        print(sides)
        return True
    else:
        print("Invalid input provided.")
        return False

def BinToHex(a):
    if set(a).issubset(bset) and set(a) != fbset:
        while len(a)%4 != 0:
            a = "0" + a
        if len(a) > 4:
            b2c = []
            for i in range(int(len(a)/4)):
                b2c.insert(0, a[-4:])
                a = a[:-4]
            a = "".join([binHexConv[x] for x in b2c])
            print(a)
        else:
            a = binHexConv[a]
            print(a)
        return True
    elif set(a) == fbset:
        a = a.split(".")
        for x in a:
            while len(a[0])%4 != 0:
                a[0] = "0" + a[0]
        left = a[0]
        right = a[1]
        if len(left) > 4:
            leftBins = []
            for i in range(int(len(left)/4)):
                leftBins.insert(0, left[-4:])
                left = left[:-4]
            left = "".join([binHexConv[x] for x in leftBins])
        else:
            left = binHexConv[left]
            print(left)
        if len(right) > 4:
            rightBins = []
            for i in range(int(len(left)/4)):
                rightBins.insert(0, left[-4:])
                right = right[:-4]
            print(right)
        else:
            right = binHexConv[right]
        print(left + "." + right)
        return True



    else:
        print("Invalid input provided.")
        return False


def DecToOct(v):
    try:
        floatv = float(v)
    except:
        print("Not a valid input.")
        return False
    else:
        if "." not in set(v):
            v += ".0"
        vsplit = v.split(".")
        l = int(vsplit[0])
        r = "0." + vsplit[1]
        b = 8
        nums = []
        while l > b:
            nums.append(int(l%b))
            l = l/b
        nums.append(int(l))
        nums.reverse()
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        loct = "".join(nums)
        roct = []
        for i in range(len(r)):
            roct.append(str(int((float(r)*8)//1)))
            r = (float(r)*8) - ((float(r)*8)//1)
        roct = "".join(roct)
        if roct[:3] == "000":
            print(loct)
        else:
            print(loct + "." + roct[:3])
        return True

def DecToBin(v):
    try:
        floatv = float(v)
    except:
        print("Not a valid input.")
        return False
    else:
        p,i = 0,0
        nums = []
        if "." not in set(v):
            v += ".0"
        vsplit = v.split(".")
        l = int(vsplit[0])
        r = vsplit[1]
        while p < l:
            p = 2**i
            nums.append(p)
            i+=1
        nums.reverse()
        nums = nums[1:]
        for i in range(len(nums)):
            if l >= nums[i]:
                l -= nums[i]
                nums[i] = "1"
            else:
                nums[i] = "0"
        lbin = "".join(nums)+"."
        rbin = []
        dotr = float("."+str(r))
        for i in range(len(r)):
            dotr = dotr*2
            rbin.append(str(int(dotr//1)))
            dotr = float(str(dotr)[1:])
        rbin = "".join(rbin)
        out = lbin + rbin
        if out [-2:] == ".0":
            print(out[:-2])
        else:
            print(out)
        return True

def DecToHex(v):
    try:
        floatv = float(v)
    except:
        print("Not a valid input.")
        return False
    else:
        rems = []
        while floatv > 16.0:
            step = floatv/16
            digRem = step - int(step)
            rem = int(digRem*16)
            rems.append(str(rem))
            floatv = float(int(step))
        rems.append(str(int(floatv)))
        hexList = list(hexConv.keys())
        for i in range(len(rems)):
            for j in list(hexConv.keys()):
                if rems[i] == hexConv[j]:
                    rems[i] = j
        print("0x" + "".join(rems[::-1]))
        return True

def HexToDec(u):
    try:
        for i in list(u):
            i in hexConv.keys() or int(i)
    except:
        print("Not a valid hex string.")
        return False
    else:
        a = list(u)[::-1]
        for i in range(len(a)):
            for j in list(hexConv.keys()):
                if a[i] == j:
                    a[i] = hexConv[j]
        #print(a)
        e = [int(i)*(16**a.index(i)) for i in a]
        print(sum(e))
        return True

def BinToDec(b):
    if set(b) != fbset:
        b += "."
    if set(b) == fbset:
        bc2sum = []
        bsplits = b.split(".")
        l = bsplits[0]
        l = list(l)
        l.reverse()
        r = bsplits[1]
        r = list(r)
        for i in range(len(l)):
            bc2sum.append((2**i)*int(l[i]))
        for i in range(len(r)):
            bc2sum.append(1/(2**(i+1))*int(r[i]))
        print(sum(bc2sum))
        return True
    else:
        print("User input is not a valid binary number.")
        return False

print("Simple Base Conversion Tool")
print("---")
print()

print("Format: [INPUT] --option")
opts = {
"--bto" : "Convert Binary to Octal",
"--btd" : "Convert Binary to Decimal",
"--bth" : "Convert Binary to Hexadecimal",
"--otb" : "Convert Octal to Binary",
"--otd" : "Convert Octal to Decimal",
"--oth" : "Convert Octal to Hexadecimal",
"--dth" : "Convert Decimal to Hexadecimal",
"--dtb" : "Convert Decimal to Binary",
"--dto" : "Convert Decimal to Octal",
"--htb" : "Convert Hexadecimal to Binary",
"--htd" : "Convert Hexadecimal to Decimal",
"--hto" : "Convert Hexadecimal to Octal"
}

print()
print("Options:")
for i in opts:
    print("["+i+"]   " + opts[i])
print()

running = True
while running == True:
    solved = False
    while solved == False:
        x = input(">")
        if x == "exit":
            running = False
            solved = True
            break
        else:
            pass
        xVal = False
        while xVal == False:
            try:
                x.split()[1][:2:] == "--"
            except:
                print("Not a valid input.")
                x = input(">")
            else:
                xVal = True
                x = x.split()
                if len(x) > 2:
                    print("Too many arguments provided.")
                elif x[1] not in opts.keys():
                    print("No valid option provided")
                else:
                    xNum = x[0]
                    xOpt = x[1]
                    if xOpt == "--htd":
                        solved = HexToDec(xNum)
                    elif xOpt == "--dth":
                        solved = DecToHex(xNum)
                    elif xOpt == "--btd":
                        solved = BinToDec(xNum)
                    elif xOpt == "--dtb":
                        solved = DecToBin(xNum)
                    elif xOpt == "--dto":
                        solved = DecToOct(xNum)
                    elif xOpt == "--bth":
                        solved = BinToHex(xNum)
                    elif xOpt == "--bto":
                        solved = binToOct(xNum)
                    elif xOpt == "--otb":
                        solved = octToBin(xNum)
                    elif xOpt == "--otd":
                        solved = octToDec(xNum)
                    elif xOpt == "--oth":
                        solved = octToHex(xNum)
                    elif xOpt == "--htb":
                        solved = hexToBin(xNum)
                    elif xOpt == "--hto":
                        solved = hexToOct(xNum)
