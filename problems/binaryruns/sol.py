# TODO: stop is fun to calculate, but maybe remove for competition? Otherwise this should be the final 100 point question.
# set FakeFraction.DEBUG to True for some good debug information.
# you can also set FakeFraction.USE_LABELS to False if you want to see the nitty gritty math.

MOD = 1000000007
b = input()

def expmod(a, b):
    res = 1 % MOD
    a %= MOD
    while b:
        if (b & 1):
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res
    
def modinv(a):
    return expmod(a, MOD-2)

# Now to calculate the probabilities! woohoo.
# For each binary string, we want to store:
# The probability that we stop there
stop = [[None, None] for _ in range(len(b) + 1)]
# The probability that we 'jump' there from a binary string with one less digit
jump = [[None, None] for _ in range(len(b) + 1)]
# And also store the longest run for each of these strings
run = [[None, None] for _ in range(len(b) + 1)]

class FakeFraction:

    DEBUG = False
    USE_LABELS = False

    def __init__(self, a, b=1, name=""):
        self.result = (a * modinv(b)) % MOD
        if FakeFraction.DEBUG:
            self.str_rep = name if FakeFraction.USE_LABELS else f"{a}/{b}"
    
    def __add__(self, other):
        n = FakeFraction(1)
        n.result = (self.result + other.result) % MOD
        if FakeFraction.DEBUG:
            n.str_rep = f"({self.str_rep} + {other.str_rep})"
        return n
    
    def __sub__(self, other):
        n = FakeFraction(1)
        n.result = (self.result - other.result) % MOD
        if FakeFraction.DEBUG:
            n.str_rep = f"({self.str_rep} - {other.str_rep})"
        return n

    def __mul__(self, other):
        n = FakeFraction(1)
        n.result = (self.result * other.result) % MOD
        if FakeFraction.DEBUG:
            n.str_rep = f"({self.str_rep} * {other.str_rep})"
        return n
    
    def repeated(self):
        n = FakeFraction(1, (1 - self.result) % MOD)
        if FakeFraction.DEBUG:
            n.str_rep = f"(1/(1-{self.str_rep}))"
        return n

    def __str__(self) -> str:
        if FakeFraction.DEBUG:
            return f"{self.result}: {self.str_rep}"
        return str(self.result)

# probabilities
one = FakeFraction(1, 1, "1")
fail = FakeFraction(1, 10000, "F")
no_fail = FakeFraction(9999, 10000, "NF")
# These already have no_fail added to them.
bad_flip = lambda x: FakeFraction(min(x, 1000) * 9999, 10000000, "BF")
good_flip = lambda x: FakeFraction((1000-min(x, 1000)) * 9999, 10000000, "GF")
bad_add = lambda x: FakeFraction(min(3*x, 10000) * 9999, 100000000, "BA")
good_add = lambda x: FakeFraction((10000-min(3*x, 10000)), 100000000, "GA")

# The indexing for both of these is a bit weird. The first index is the length of the string. And the second index is whether the last digit agrees with b or not.
# So stop[3][0] is for 001 if b is 000.

def longest_run(length, agrees):
    if run[length][agrees] is not None:
        return run[length][agrees]
    if length == 1:
        return 1
    if agrees and b[length-1] == b[length-2]:
        run[length][agrees] = longest_run(length-1, True) + 1
    elif not agrees and b[length-1] != b[length-2]:
        run[length][agrees] = longest_run(length-1, True) + 1
    else:
        run[length][agrees] = 1
    return run[length][agrees]

def solve_stop(length, agrees):
    if stop[length][agrees] is not None:
        return stop[length][agrees]
    if length == 1:
        # Bit different, since we always try to add a digit.
        # Read the other case before this one.
        jump_across = bad_add(1)
        prob1 = solve_jump(length, agrees) * fail * (jump_across * jump_across).repeated()
        prob2 = solve_jump(length, not agrees) * fail * jump_across * (jump_across * jump_across).repeated()
        prob = prob1 + prob2
        stop[length][agrees] = prob
        return stop[length][agrees]
    # If we stop here, there are two possibilities:
    # 1: We got here jumping down to this same string.
    # 2: We got here jumping down to the same string with the last bit flipped.
    prob = 0
    prob1 = solve_jump(length, agrees)
    # Now to stop here, we either:
    # Fail the first command
    # Jump left, right, then fail.
    # Jump left, right, left, right, then fail.
    # pr(stop) = fail(1 + pr(left right) + pr(left right)^2...)
    # pr(stop) = fail/(1 - pr(left right))
    we_are_good = agrees == (b[length-1] == b[length-2])
    if we_are_good:
        across_to_us = no_fail - bad_flip(longest_run(length, not agrees))
        across_from_us = bad_add(longest_run(length, agrees))
    else:
        across_to_us = bad_add(longest_run(length, not agrees))
        across_from_us = no_fail - bad_flip(longest_run(length, agrees))
    prob1 = prob1 * fail * (across_to_us * across_from_us).repeated()
    prob2 = solve_jump(length, not agrees)
    # Now to stop here, we:
    # Jump across and fail
    # Jump across and back and across and fail...
    # pr(stop) = fail*across(1 + pr(back + across) + ...)
    # pr(stop) = fail*across/(1 - pr(back + across))
    prob2 = prob2 * fail * across_to_us * (across_to_us * across_from_us).repeated()
    prob = prob1 + prob2
    stop[length][agrees] = prob
    return stop[length][agrees]

def solve_jump(length, agrees):
    if jump[length][agrees] is not None:
        return jump[length][agrees]
    # Same sort of argument, but we don't stop, we jump.
    if length == 1:
        # Just a 50/50
        return FakeFraction(1, 2, "1/2")
    # We jumped to an agreeing or disagreeing bit.
    prob1 = solve_jump(length-1, False)
    prob2 = solve_jump(length-1, True)
    # Note that whether we agree or not does not affect this question. We just care if we jump from an agreeing bit before.
    # Did rachel want to jump from the previous position to reach us?
    if length == 2:
        across_to_us = bad_add(longest_run(length-1, True))
        across_from_us = bad_add(longest_run(length-1, True))
        success = good_add(longest_run(length - 1, True)) * FakeFraction(1, 2, "1/2")
    else:
        we_are_good = b[length-2] == b[length-3]
        if we_are_good:
            across_to_us = good_flip(longest_run(length-1, False))
            across_from_us = bad_add(longest_run(length-1, True))
            success = good_add(longest_run(length - 1, True)) * FakeFraction(1, 2, "1/2")
        else:
            across_to_us = bad_add(longest_run(length-1, False))
            across_from_us = good_flip(longest_run(length-1, True))
            success = bad_flip(longest_run(length-1, True)) * FakeFraction(1, 2, "1/2")
    prob1 = prob1 * success * across_to_us * (across_to_us * across_from_us).repeated()
    prob2 = prob2 * success * (across_to_us * across_from_us).repeated()
    prob = prob1 + prob2
    jump[length][agrees] = prob
    return jump[length][agrees]

# First, precalc to avoid MLE
for length in range(1, len(b)):
    for flip in range(2):
        solve_jump(length, flip)

# The probability that we pass by is equal to the probability that we jump to this bit, or jump to the other bit and jump across
jump_on = solve_jump(len(b), True)
jump_close = solve_jump(len(b), False)
if len(b) == 1 or b[-1] != b[-2]:
    # We always try to get a new bit
    jump_close = jump_close * bad_add(1)
else:
    # We want to flip
    jump_close = jump_close * good_flip(longest_run(len(b), False))
total = jump_on + jump_close
if FakeFraction.DEBUG:
    print(
        f"Chance to jump to {b} -> {jump_on}", 
        f"Chance to jump to {b[:-1] + ('0' if b[-1] == '1' else '1')} -> {jump_close}", 
        f"Chance to see {b} -> {total}", 
        sep="\n\n"
    )
else:
    print(total)
