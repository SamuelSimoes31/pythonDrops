while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      a = float(input('Numer 1: '))
      b = float(input('Numer 2: '))
      print(a+b)
   elif user_input == "subtract":
      a = float(input('Numer 1: '))
      b = float(input('Numer 2: '))
      print(a-b)
   elif user_input == "multiply":
      a = float(input('Numer 1: '))
      b = float(input('Numer 2: '))
      print(a*b)
   elif user_input == "divide":
      a = float(input('Numer 1: '))
      b = float(input('Numer 2: '))
      print(a//b)
   else:
      print("Unknown input")
quit()