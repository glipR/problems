import sys

r = input()
e = input()

key = "professor"
if key in r and key in e:
    print(-1)
    sys.exit()

# We can definitely finish this, so just do it.
while key in e:
    e = e.replace(key, r, 1)

print(len(e))