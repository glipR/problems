import re

hiss = re.compile("^hiss+$")
trill = re.compile("^tri+ll+$")
burble = re.compile("^bu+r+bl+e$")

t = int(input())
for i in range(t):
    s = input()
    if hiss.match(s) is not None:
        print("hiss")
    elif trill.match(s) is not None:
        print("trill")
    elif burble.match(s) is not None:
        print("burble")
    else:
        print("human noises")