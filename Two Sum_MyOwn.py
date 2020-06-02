nums = [2,3,4,7, 11, 15]
target = 9

for n in range(len(nums)):
    for m in range(len(nums)):
        if target == nums[n] + nums[m]:
            if n == m:
                continue
            else:
                print(n, m)
        else:
            continue