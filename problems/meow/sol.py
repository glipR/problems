t = int(input())
for case in range(t):
    s = input()
    found = False
    # Meow
    if len(s) >= 4 and s[0] == "m":
        try:
            b1, b2 = s[1:].split("o")
            if b1 == "e" * len(b1) and b2 == "w" * len(b2) and len(b1) > 0 and len(b2) > 0:
                found = True
                print("meow")
        except:
            pass
    # Purr
    if not found and len(s) >= 4 and s[0:4] == "purr":
        if s[4:] == "r" * len(s[4:]):
            print("purr")
            found = True
    # Roar
    if not found and len(s) >= 4 and s[0] == "r":
        if s[-2:] == "ar" and s[1:-2] == "o" * (len(s[1:-2])) and len(s[1:-2]) > 0:
            print("roar")
            found = True
    if not found:
        print("human noises")
