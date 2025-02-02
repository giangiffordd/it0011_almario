def count():
    i = input("Please enter a string: ")
    
    v = 0
    c = 0
    s = 0
    o = 0

    i = i.lower()

    for char in i:
        if char in 'aeiou':
            v += 1
        elif char in 'bcdfghjklmnpqrstvwxyz':
            c += 1
        elif char == ' ':
            s += 1
        else:
            o += 1
            
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")
    print(f"Spaces: {s}")
    print(f"Other characters: {o}")

count()
