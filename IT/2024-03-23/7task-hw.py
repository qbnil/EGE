number = (27**1166+9**937)*81**1852 - 2
twoCounter = 0
zeroCounter = 0
while number > 0:
    ost = number%3
    if ost == 0:
        zeroCounter+=1
    elif ost == 2:
        twoCounter+=1
    number = number//3
print(twoCounter-zeroCounter)
    
