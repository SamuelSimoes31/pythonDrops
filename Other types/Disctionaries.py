ages = {"Dave": 24, "Mary": 42, "John": 58,"Dave": 45}
print(ages["Dave"])
print(ages["Mary"])

#keyError
primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])
print(primary["yellow"])

#TypeError
bad_dict = {
  [1, 2, 3]: "one two three", 
}

'''
Here's the list of class that are immutable:

1. Bool 
2. int 
3. float 
4. tuple
5. str 
6. frozen set            

And Here's the list of class that are mutable:

1. list
2.set
3.dict
'''

#adding
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

#checking
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#get
pairs = {
  1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(1))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))