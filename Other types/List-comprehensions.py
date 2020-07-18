# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
# range 5 means from 0 to 4
# giving (0, 1, 2, 3, 4.) making 5 in total.
# and the key is x**3.
# so;
# 0**3= 0×0×0= 0
# 1**3= 1×1×1= 1
# 2**3= 2×2×2= 8
# 3**3= 3×3×3= 27
# 4**3= 4×4×4= 64

nums = [i*2 for i in range(10)]
print(nums)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

evens=[i for i in range(10) if i % 2 == 0]
print(evens)

# DON'T
# # even = [2*i for i in range(10**100)]