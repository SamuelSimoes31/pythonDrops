nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
msg = "Numbers: {1} {2} {0}".format(nums[0], nums[1], nums[2])
print(msg)


# A couple of things to note:
# 1.    You don't always need numbers in the curly brackets.  If you leave them blank, the format items listed are inserted in order, e.g.
nums = [4, 5, 6]
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg)
# outputs Numbers: 4 5  6

# You can use them to change the order of insertion, e.g.
nums = [4, 5, 6]
msg = "Numbers: {2} {0} {0}".format(nums[0], nums[1], nums[2])
print(msg)
# outputs Numbers: 6 4 4

# 2.    Although nums are integers, when they are inserted into a string with format, they are no longer integers, e.g.
nums = [4, 5, 6]
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg)
print(msg[0])
print(msg[9])
print(msg[11])
print(msg[9] + msg[11])
print(int(msg[9]) + int(msg[11]))


a = "x={x},y={y}".format(x=5, y=12)
print(a)


a = "{0}, {1}, {x}, {y}".format(1, 3, x=5, y=12)
print(a)
# >>>1, 3, 5, 12
# but:
a = "{0}, {1}, {x}, {y}, {2}".format(1, 3, x=5, y=12,15)
print(a)
# >>> SyntaxError

a = "{0}, {1}, {x}, {y}, {2}, {3}".format(1, 3, 33, 44, x=5, y=7)
print(a)
# >>>1, 3, 5, 7, 33, 44 