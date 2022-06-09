import math
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def fibonacci(n):
    sQ = [0,1]
    for i in range(2,n+1):
        newNum = sQ[-1] + sQ[-2]
        sQ.append(newNum)
    return sQ

def primeCheck(number):
    if number > 2 and number % 2 == 0:
        return False
    upperDivision = math.floor(math.sqrt(number))
    for i in range(3, 1 + upperDivision, 2):
        if number % i == 0:
            return False
    return True

def primeToString(p):
    p = str(p)
    result = ""
    for i in range(0, 10, 2):
        index = p[i:i+2]
        index = int(index)
        index = index % 26
        result = result + alphabet[index]
    return result

if __name__ == '__main__':
    done = False
    found = []
    while done == False:
        numbFound = 0
        fibs = fibonacci(11000)
        strg = ""
        for j in fibs:
            if j != 0:
                strg = strg + str(j)
        for i in range(0, len(strg)):
            newstr = strg[i:i+10]
            newstr = int(newstr)
            if len(str(newstr)) == 10:
                if primeCheck(newstr):
                    if newstr in found:
                        print("Same")
                    if (newstr in found) == False:
                        numbFound = numbFound + 1
                        found.append(newstr)
                        if numbFound == 1:
                            print(newstr)
                        if (numbFound == 44722):
                            print("44722nd:", newstr)
                            print(primeToString(newstr))
                        if (numbFound == 53215):
                            print("53215th:", newstr)
                            print(primeToString(newstr))
                            break
        done = True
