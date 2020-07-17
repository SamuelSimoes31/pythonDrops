array = ['zero','um','dois']
n = -3
while n<3:
    print(n,array[n])
    n = n+1

empty_list = []
print(empty_list)
print(len(empty_list))

a = [2, ""]
b = [2,]
c = [2, " "]

print(len(a))
print(len(b))
print(len(c))

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[0][2])
print(things[1])
print(things[2])
print(things[2][2])

words = "I love learning Python using Sololearn!".split()
print(words)

a = ['x' , 'y']
b = a
b[0] = 'z'
print(b) #output: ['z' , 'y'] no surprise
print(a) #!!!output!!!: ['z' , 'y']

c = ['x' , 'y']
d = c.copy()
d[0] = 'z'
print(d) 
print(c)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

s ='i love humanity'
a =list(s)
print (a)
#output : ['i', ' ', 'l', 'o', 'v', 'e', ' ', 'h', 'u', 'm', 'a', 'n', 'i', 't', 'y']

s ='i love humanity'.split()
print (s)
#output : ['i', 'love', 'humanity']

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print("washer" in  tools[3])
#^Yields "true"

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print("washer" in  tools)
#^Yields "false"

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print(tools[2][3:5] in  tools[4])
#^Yields "true"

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print(tools[2][3:5] in  tools)
#^Yields "false"

nums = [1, 2, 3]
print('not 4 in nums',not 4 in nums)
print('4 not in nums',4 not in nums)
print('not 3 in nums',not 3 in nums)
print('3 not in nums',3 not in nums)

spam = [1,2]
eggs = spam # so eggs = [1,2]
spam = [1,2,3] #changing the value of spam
print(eggs) # variable 'eggs' is not updated and output is [1,2]

spam = [1,2]
eggs = spam
bacon = eggs
spam.append(3)
print(spam)  # output is [1,2,3]
print(eggs)  # output also is [1,2,3]
print(bacon) # output also is [1,2,3]

#Additionally - 'spam += [3]' and 'spam = spam.insert(2,3)' also update both 'bacon' and 'eggs'  to [1,2,3]

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

aaa = []
aaa.append(1)
print(aaa)

listt = [1,2,3]
obj = 2
max(listt) # Returns the list item with the maximum value
min(listt) # Returns the list item with minimum value
listt.count(obj) # Returns a count of how many times an item occurs in a list
listt.remove(obj) # Removes an object from a list
listt.reverse() # Reverses objects in a list

numbers = list(range(10))
print(numbers)

a = range (10, 20, 2) #creates a range from 10 to 20 every 2 steps
b = list(a)
print(a)
print (b)

print(range(20) == range(0, 20))

numbers = list(range(0, 10, -2))
print(numbers)
numbers = list(range(10, 0, -2))
print(numbers)

words = ["hello", "world", "spam", "eggs"]

counter = 0
max_index = len(words) - 1
while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1 

for word in words:
  print(word + "!")

for i in range(5):
  print("hello!",i)

  letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])

