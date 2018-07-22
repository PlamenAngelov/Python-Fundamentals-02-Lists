nums = list(map(float, input().split(' ')))

adjacent_flag = True

while adjacent_flag:
    adjacent_flag = False
    for i in range(0,len(nums)-1):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            nums.pop(i)
            nums[i] *= 2
            adjacent_flag = True
            break

for num in nums:
    print(f"{num:.2g}", end = ' ')
