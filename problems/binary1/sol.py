import sys

index = int(input())

bit_length = 1

while index > (1 << (bit_length-1)) * bit_length:
    index -= (1 << (bit_length-1)) * bit_length
    bit_length += 1

# 0 index.
index -= 1
# Our number has this bit_length.
skip_num = index // bit_length
actual_num = (1 << (bit_length-1)) + skip_num

index = index % bit_length

print(bin(actual_num)[2:][index])
