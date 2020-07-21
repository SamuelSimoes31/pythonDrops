def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

def f(x):
  return x*2
f(3) # >>> 6

g = lambda x: x*2
g(3) # >>> 6
(lambda x: x*2)(3) # >>> 6




#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

double = lambda x: x * 2
print(double(7))
sum = lambda x, y: x + y
print(sum(7,8))

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))