num = (6561**1346 + 729**1473) * 9**820 - 81
zeroCounter = 0
eightCounter = 0
finalN = ''
while num > 0:
    ost = num%9
    finalN = finalN + str(ost)
    num //= 9
print(finalN.count('8') - finalN.count('0'))
