import sys

index = int(input())

total = []

num = 1
while index > 0:
   last_num = bin(num)[2:]
   total.extend(list(last_num))
   num += 1
   index -= len(last_num)

# index = 0 => final index last_num
# index = -a => first index of last_num

print("".join(total[:100]), file=sys.stderr)
print(total[:len(total)+(index-1) + 1].count("1"))

