'''
FILE MODES:

"r"
Read from file - YES
Write to file - NO
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"r+"
Read from file - YES
Write to file - YES
Create file if not exists - NO
Truncate file to zero length - NO
Cursor position - BEGINNING

"w"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"w+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - YES
Cursor position - BEGINNING

"a"
Read from file - NO
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END

"a+"
Read from file - YES
Write to file - YES
Create file if not exists - YES
Truncate file to zero length - NO
Cursor position - END
'''

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open("filename.txt", "r")
print("Reading")
print(file.read())
print("Re-reading")
print(file.read())
print("Finished")
file.close()

file = open("filename.txt", "r")
print(file.readlines())
file.close()

file = open("filename.txt", "r")
for line in file:
  print(line)
file.close() 

# WRITING -----------------------------------------
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# exceptions ----------------------------------------------------
try:
  f = open("filename2.txt")
  print(f.read())
except FileNotFoundError:
  print("No such file or directory")
finally:
  try:
    f.close()
  except:
    print("Can't close file")

with open("filename.txt") as f:
  print(f.read())

try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)