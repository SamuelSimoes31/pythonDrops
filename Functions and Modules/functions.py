def my_func():
  print("spam\n" * 3)

my_func()
my_func()
 
#------------------------------------------------------------------------------------------
 
def print_with_exclamation(word):
  print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
 
#------------------------------------------------------------------------------------------
 
def function(variable):
  variable += 1
  print(variable)

function(7)
# print(variable) # variable not defined
# Arguments can be changed every time you call the function. Parameters are used when defining the function. In the example shown,  (variable)  is a PARAMETER and (7) is the ARGUMENT.
 
#------------------------------------------------------------------------------------------
 
def even(x):
  if x%2 == 0:
    print("Yes")
  else:
    print("No")
even(3)
even(4)
 
#----RETORNO--------------------------------------------------------------------------------------
 
def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)
 
#----RETORNO--------------------------------------------------------------------------------------
 
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))