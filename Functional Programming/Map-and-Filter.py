nums = [11, 22, 33, 44, 55]

def add_five(x):
  return x + 5
result = list(map(add_five, nums))
print(result)

result = list(map(lambda x: x+5, nums))
print(result)
# map() returns a new itarable

nums = [i*11 for i in range(1,6)]
result = [n + 5 for n in nums]
print(result)

a = list(map(lambda x: x*2,nums))
a = [x*2 for x in nums]

#--------------------------------------------------

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

res = [x for x in nums if x%2==0]
print(res)