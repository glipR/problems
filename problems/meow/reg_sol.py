import re

meow = re.compile("^me+ow+$")
purr = re.compile("^purr+$")
roar = re.compile("^ro+ar$")

t = int(input())
for i in range(t):
    s = input()
    if meow.match(s) is not None:
        print("meow")
    elif purr.match(s) is not None:
        print("purr")
    elif roar.match(s) is not None:
        print("roar")
    else:
        print("human noises")