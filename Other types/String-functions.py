print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("|".join(["spam", "eggs", "ham"]))
#prints "spam|eggs|ham"

#=============================================

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("Hello MEME ME ME".replace("ME", "world"))
#prints "Hello worldworld world world"

#=============================================

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

#=============================================

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

#=============================================

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

#=============================================

sent = "Hello have a nice day"
print(sent)
# Output: Hello have a nice day
sent1 = sent.split(" ")
print(sent1)
#Output: ['Hello', 'have', 'a', 'nice', 'day']
sent1[3] = "super"
sent2 = " ".join(sent1)
print(sent2.upper())
#Output: HELLO HAVE A SUPER DAY
sent3 = sent2.replace("day", "week")
print(sent3.lower())
#Output: hello have a super week


txt=[">","<"]
for i in range(1,10):
  str="@"*i
  print(str.join(txt))
# >@<
# >@@<
# >@@@<
# >@@@@<
# >@@@@@<
# >@@@@@@<
# >@@@@@@@<
# >@@@@@@@@<
# >@@@@@@@@@<