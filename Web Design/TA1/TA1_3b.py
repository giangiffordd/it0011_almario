def TA_3b():
    v = 1
    while v <= 7:
        if v == 2 or v == 4:
            v += 1
            continue
        
        spaces = 0
        while spaces < v:
            print(v, end="")
            spaces += 1
        print()
        v += 1

TA_3b()
