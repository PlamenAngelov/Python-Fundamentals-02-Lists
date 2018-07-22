nums = list(map(int, input().split(' ')))

nums_len = len(nums)-1
for i in range(0, int(len(nums)/2)):
    temp = nums[nums_len - i]
    nums[nums_len - i] = nums[i]
    nums[i] = temp

print(" ".join(map(str, nums)))
