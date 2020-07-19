with open('text.txt') as f:
  text = f.read()
print(text)
# print(for x in text)

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

freq = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    freq[c] = 0

# doc = text.lower()
doc = text
for c in doc:
  for char in "abcdefghijklmnopqrstuvwxyz":
    if c == char:
      freq[char] += 1
      break

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * freq[char] / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))