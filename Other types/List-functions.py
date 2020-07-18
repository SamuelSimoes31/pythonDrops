nums = [55, 44, 33, 22, 11]

print([i > 5 for i in nums])
if all([i > 5 for i in nums]):
  print("All larger than 5")

print([i % 2 == 0 for i in nums])
if any([i % 2 == 0 for i in nums]):
  print("At least one is even")

for v in enumerate(nums):
  print(v)
for v in enumerate(nums,-1):
  print(v)
for v in enumerate(nums,-4):
  print(v)


nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)