import sys

repeats, jump = list(map(int, input().split()))

total = []

num = jump
for _ in range(repeats):
   last_num = bin(num)[2:]
   total.extend(list(last_num))
   num += jump

# index = 0 => final index last_num
# index = -a => first index of last_num

print("".join(total[:100]), file=sys.stderr)
print(total.count("1"))

