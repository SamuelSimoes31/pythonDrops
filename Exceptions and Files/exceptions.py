# Exceptions

# Different exceptions are raised for different reasons.
# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type; EX: print("7" + 4)
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.

# HANDLING

try:
  num1 = 7
  num2 = 0
  print (num1 / num2)
  print("Done calculation")
except ZeroDivisionError:
  print("An error occurred")
  print("due to zero division")
except TypeError:
  print ("You didn't type a number")

try:
  X=6
  y=4
  print(X+Y)
except:
  print("something is wrong")

try:
  variable = 10
  print(variable + "hello")
  print(variable / 2)
except ZeroDivisionError:
  print("Divided by zero")
except (ValueError, TypeError):
  print("Error occurred")
  print(ValueError, TypeError)

try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")
finally:
  print('BOA')

  # https://realpython.com/the-most-diabolical-python-antipattern/

try:
  print("1"+1)
except ZeroDivisionError:
  print("Divided by zero")
# except TypeError:
#   print("TypeError")
finally:
  print("This code will run")
print("This code will NOT run")

try:
  print(1)
  print(10 / 0)
except ZeroDivisionError:
  print(unknown_var)
finally:
  print("This is executed last")

# try:
#   print("1"+1)
# except ZeroDivisionError:
#   print("Divided by zero")
# # except TypeError:
# #   print("TypeError")
# finally:
#   print("This code will run")
# print("This code will NOT run")

print(1)
raise ValueError
print(2)

password = input("enter password")
if len(password) < 8:
  raise ValueError("password should be more than 8 characters")


#Try this one:
password = input("enter password: ")
if len(password) < 8:
  raise ValueError("password should be more than 8 characters")
else: print(password)

try:
  num = 5 / 0
except:
  print("An error occurred")
  raise

name = "123"
raise NameError("Invalid name!")

'''
Assertions vs Try/Except :

Assertion is a condition which is critical for the code execution. An assertion would stop the program from running(because you should fix that error or the program is useless, but an exception would let the program continue running.
In other words, exceptions address the robustness of your application while assertions address its correctness.

Assertions should be used to check something that should never happen (authorize your code logic), while an exception should be used to check something that might happen(something you don't control like user input).

use assertions when checking pre-conditions, post-conditions in code.
use assertions to provide feedback to yourself or your developer team.
use assertions when checking for things that are very unlikely to happen otherwise it means that there is a serious ﬂaw in your application.
use assertions to state things that you (supposedly) know to be true.
'''

print(0)
assert "h" != "w"
print (1)
assert False
print(2)
assert True
print(3)

temp = -10
assert (temp >= 0), "Colder than absolute zero!"