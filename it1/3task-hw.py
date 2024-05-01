for n in range(10000):
    binary = bin(n)[2:]
    if binary.count('1') % 2 == 0:
        binary = '10' + binary[2:] + '1'
    else:
        binary = '11' + binary[2:] + '0'
    int_n = int(binary, 2)
    if int_n < 88:
        print(int_n, n)
