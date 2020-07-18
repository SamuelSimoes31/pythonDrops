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