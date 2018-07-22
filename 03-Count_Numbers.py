nums = sorted(list(map(int, input().split(' '))))
counts = []

for num in nums:
    if not num in counts:
        counts.append(num)

for n in counts:
    print(f"{n} -> {nums.count(n)}")
