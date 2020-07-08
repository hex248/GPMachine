def decimalToHex(x):
    n = x
    if x <= 255:
        if x >= 128:
            bit8 = "1"
            x = x - 128
        else:
            bit8 = "0"
        if x >= 64:
            bit7 = "1"
            x = x - 64
        else:
            bit7 = "0"
        if x >= 32:
            bit6 = "1"
            x = x - 32
        else:
            bit6 = "0"
        if x >= 16:
            bit5 = "1"
            x = x - 16
        else:
            bit5 = "0"
        if x >= 8:
            bit4 = "1"
            x = x - 8
        else:
            bit4 = "0"
        if x >= 4:
            bit3 = "1"
            x = x - 4
        else:
            bit3 = "0"
        if x >= 2:
            bit2 = "1"
            x = x - 2
        else:
            bit2 = "0"
        if x >= 1:
            bit1 = "1"
            x = x - 1
        else:
            bit1 = "0"
        binary = bit8 + bit7 + bit6 + bit5 + bit4 + bit3 + bit2 + bit1
        binary1 = binary[:4]
        binary2 = binary[4:8]
        def fourBitToHex(b1, b2):
            h1 = 0
            h2 = 0
            if b1[0] == "1":
                h1 += 2 ** 3
            if b1[1] == "1":
                h1 += 2 ** 2
            if b1[2] == "1":
                h1 += 2 ** 1
            if b1[3] == "1":
                h1 += 2 ** 0
            if b2[0] == "1":
                h2 += 2 ** 3
            if b2[1] == "1":
                h2 += 2 ** 2
            if b2[2] == "1":
                h2 += 2 ** 1
            if b2[3] == "1":
                h2 += 2 ** 0
            return hex(h1)[2:] + hex(h2)[2:]
        print("\n""The hexadecimal of", n, "is:", fourBitToHex(binary1, binary2))
    else:
        print("\n""ERROR: Decimal number is higher than 255")
decimalToHex(1)