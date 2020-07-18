words = ("spam", "eggs", "sausages",)

#tuples themselve are immutable but the content of mutable elements (like lists) inside a tuple can be changed!

t = (1, "hungry", ['x' , 'y'])
t[0] = 234
#results in a type error because t is immutable

t = (1, "hungry", ['x' , 'y'])
t[2][0] = 'abc'
print(t)
#output is: (1, "hungry", ['abc' , 'y'])
#so the content of the list inside the tuple IS mutable

my_tuple = "one", "two", "three"
print(my_tuple[0])

tuple = (1, (1, 2, 3))
print(tuple[1])