import sys

index = int(input())

total_ones = 0
bit_length = 1

while index > (1 << (bit_length-1)) * bit_length:
    index -= (1 << (bit_length-1)) * bit_length
    if bit_length == 1:
        total_ones += 1
    else:
        total_ones += (1 << (bit_length-2)) * (bit_length + 1)
    print(total_ones, bit_length, file=sys.stderr)
    bit_length += 1

# 0 index.
index -= 1
# Our number has this bit_length.
skip_num = index // bit_length
actual_num = (1 << (bit_length-1)) + skip_num

def rec(prev_ones, min_val, max_val, power):
    global total_ones
    if power < 0:
        return
    print(f"{min_val} {max_val} jump {1 << power} ones {prev_ones}", file=sys.stderr)
    # min_val is always a power of 2
    # max_val is either a power of 2 or smaller.
    if min_val + (1 << power) <= max_val:
        # We can skip to the right half
        total_ones += (1 << power) * prev_ones
        print(f"{(1 << power) * prev_ones} ones added from previous indicies", file=sys.stderr)
        if power > 0:
            total_ones += (1 << (power-1)) * power
            print(f"{(1 << (power-1)) * power} extra ones in the left half added", file=sys.stderr)
            rec(prev_ones+1, min_val + (1 << power), max_val, power-1)
    else:
        # We are in the left half
        if power > 0:
            rec(prev_ones, min_val, max_val, power-1)

print(f"Num lives in {actual_num}", file=sys.stderr)
rec(1, 1 << (bit_length-1), actual_num, bit_length-2)

index = index % bit_length
# Doesn't count the final number.
total_ones += bin(actual_num)[2:][:index+1].count("1")

print(total_ones)
