import sys

my_list = []
special, noccurences = list(map(int, input().split("_")))

cur_num = 1
special_included = 0
while special_included < noccurences:
    factors = []
    after_special = 0
    for step in range(1, cur_num+1):
        if cur_num % step == 0:
            if step == special:
                special_included += 1
            if step > special:
                after_special += 1
            factors.append(f"{step}_{cur_num//step}")
    my_list.extend(factors)
    cur_num += 1

print(my_list[:1000], file=sys.stderr)
print(len(my_list) - after_special)
