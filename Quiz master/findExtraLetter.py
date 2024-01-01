def getExtraLetter(s, t):
    chs={}
    for ch in list(t):
        if ch not in list(s):
            return ch

s = input("Enter a string ")
t = input("Enter modified string with extra letter ")
ch = getExtraLetter(s, t)
print("extra letter =", ch)