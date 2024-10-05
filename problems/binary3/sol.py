from math import log2, floor, ceil
import sys

DEBUG = False

repeats, jump = list(map(int, input().split()))
if DEBUG:
    print(f"{repeats} {jump}", file=sys.stderr)

while jump % 2 == 0:
    jump //= 2

print(jump)

total_ones = 0
handled_bit_length = floor(log2(repeats))

# Handle the first handled_bit_length bits.
total_ones += (1 << (handled_bit_length - 1)) * handled_bit_length if handled_bit_length >= 1 else 0

if DEBUG:
    print(f"Handled {total_ones} ones in the known block.", file=sys.stderr)

# Now we need to count the occurence of all digits before this in the sequence.
def rec(minval, maxval, cur_bit):
    global total_ones
    # print(minval, maxval, cur_bit)
    if cur_bit <= handled_bit_length - 1:
        return
    midway = minval + (1 << cur_bit)
    if midway <= maxval:
        if DEBUG:
            print(f"{maxval // jump - (midway-1) // jump} values in [{midway}, {maxval}], and all of these have a 1 in the {cur_bit}th bit.", file=sys.stderr)
        total_ones += maxval // jump - (midway-1) // jump

        rec(midway, maxval, cur_bit-1)
    rec(minval, min(midway-1, maxval), cur_bit-1)

print(0, repeats*jump)
rec(0, repeats*jump, ceil(log2(repeats * jump)))

print(total_ones)
