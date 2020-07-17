import random # fully

for i in range(5):
  value = random.randint(1, 6)
  print(value)

from math import pi #just one
print(pi)

from math import sqrt, cos #various
import math
print(math.cos == cos)

from math import sqrt as square_root #import as a diferent name
print(square_root(100))
from math import sqrt as square_root, cos as cosine, tan as tangent
print(square_root(49))
print(cosine(0))
print(tangent(45))

print( dir(math) ) 

import math as m
print(math.sqrt(25))