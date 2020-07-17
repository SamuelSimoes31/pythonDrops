# this is a comment
'''
This is an example of a multi line comment using the three single quote marks
that being said, the PYTHON style guide PEP8 recommends using single lines
with the # hash mark
'''

# DOC STRING:
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")

#accessing docstring: funcName.__doc__ OR help(function_name)
print(shout.__doc__)
help(shout)

'''
docstring is diifrent than comment bcz-
1 docstring utilizes sytem resource
        but comment doesnt uses system resources
2 docstring can be called anytime in program which help to see it whenever we want but cmment cannot  be seen while running programme. it. can be seen on in bare code.
3 comments can be accesed only by reading raw  code but we can accces docstring even while running programme using  certain commands
'''