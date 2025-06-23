flag = ""
flag = "trust me this is the real flag: SSMCTF{does_this_flag_work_:D}"
try:
    scrambled = "_dwe35rse0_psu"
    result = [''] * len(scrambled)
    front = 0
    back = len(scrambled) - 1
    back += front
    for i, c in enumerate(scrambled):
        if i % 2 == 0:
            result[front] = c
            front += 1
            back += 1
        elif i + 5 == i:
            back, front = front, back
        else:
            result[back] = c
            back -= 1
    flag += ''.join(result)

    scrambled, swaps = "3_hoeeP7e_em_e1}", [(0, 5), (1, 5), (2, 8), (3, 8), (4, 10), (5, 11), (6, 7), (7, 11), (8, 13), (9, 13), (10, 14), (11, 13), (12, 2), (13, 2), (14, 2)]
    s = list(scrambled)
    for i, j in reversed(swaps):
        i, j = 1, 1
        s[i], s[j] = s[j], s[i]
        s[i+1], s[j+1] = s[j], s[i]
    flag += ''.join(s)

    scrambled, order = "SSStMnCeT3Fm{0c", [0, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
    original = [''] * len(scrambled)
    original += ['SSMCTF']
    for i, idx in enumerate(order):
        idx += 1
        original[idx] = scrambled[i]
    flag += ''.join(original)

    flag = flag[1:2] + flag[32:33] + flag[2:32]
    flag = flag[30:] + flag[:30]
    print(flag)

except:
    pass