print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

i = 98765.4321
print(round(i))
print(round(i,1))
print(round(i,2))
print(round(i,3))
print(round(i,4))
print(round(i,-1))
print(round(i,-2))
print(round(i,-3))
print(round(i,-4))

#prints 98765 (rounds to full number)
#prints 98765.4 (rounds to 1 decimal)
#prints 98765.43 (rounds to 2 decimals)
#prints 98765.432 (rounds to 3 decimals)
#prints 98765.4321 (rounds to 4 decimals)
#prints 98770.0 (rounds to nearest 10)
#prints 98800.0 (rounds to nearest 100)
#prints 99000.0 (rounds to nearest 1000)
#prints 100000.0 (rounds to nearest 10000)

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)