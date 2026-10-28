ch=input("donner ch")
s = 0
signe = 1
nb = 0
for i in range(len(ch)):
    if ch[i].isdecimal():
        nb = nb * 10 + int(ch[i])
    else:
        s = s + signe * nb
        nb = 0
        if ch[i] == "+":
            signe = 1
        else:
            signe = -1
s = s + signe * nb
print(s)