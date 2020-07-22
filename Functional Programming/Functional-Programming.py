#  https://pt.stackoverflow.com/questions/11403/diferen%C3%A7a-entre-fun%C3%A7%C3%B5es-de-alta-ordem-e-primeira-classe#:~:text=Fun%C3%A7%C3%A3o%20de%20alta%20ordem%20%C3%A9,ela%20%C3%A9%20ou%20n%C3%A3o%20%C3%A9.
# https://en.wikipedia.org/wiki/Higher-order_function
# https://en.wikipedia.org/wiki/First-class_function

'''
Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.
'''

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

some_list = []
def impure(arg):
  some_list.append(arg)

'''
If the answer to all questions is "yes", your function is pure.

1. Does my function depend only on its arguments and nothing else? OR Does my function always return the same result given the same arguments?
2. Can I run my function anywhere in the script without causing any trouble or side effects whatsoever?
3. Can I run my function with the same arguments many times and still return the same result each time?
4. Is it true that my function does not change anything outside it, but only returns something?
5. Can my function be used by other functions or scripts with equal success?
'''

#PURE
z="I didn't changed"
y="I also didn't changed"
def func(x):
  y=x**2
  z=x+y
  return z

func(5)
print(z)
print(y)
print(func(5))

#IMPURE
z="I did changed"
y="I also did changed"

some_list = []

def impure(arg):
  some_list.append(arg)
  
impure(z)
print(some_list)
impure(y)
print(some_list)

# >> [I did changed]
# >> [I did changed,I also did changed]



# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
# - easier to run in parallel.
# The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects.
# They can also be more difficult to write in some situations

'''
https://en.wikipedia.org/wiki/Memoization
MEMOIZATION EXPLAINED
Memoization is whereby the result of a previous section can be referred and used to get the result of the next without having to go through a lot of work.
Example.
If you write
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
and asked for an answer, you will take time to do that and get 10
Now if I add another +1 at the end
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
You will instantly say 11
That is memoization. You will not go back to adding the whole list of 1s.
Practical example can be in calculation of factorials.
Once you know that 3! is 6 (ie 1 * 2 * 3) then if I asked you 4! you simply take 3! * 4 = 24 other than doing it over again as 1 * 2 * 3 * 4
Now let us apply Memoization:
9! = 362880
find 10!
Answer: Simply 9! * 10 = 3628800
'''

