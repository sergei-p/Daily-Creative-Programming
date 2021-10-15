import random
import time

r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 = " " * 10
while 1 != 0:
  x1 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x2 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x3 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x4 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x5 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x6 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x7 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x8 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x9 = " " if random.randint(1,10) % 2 == 0 else "*" 
  x10 = " " if random.randint(1,10) % 2 == 0 else "*" 

  r1 = "%s %s %s %s %s %s %s %s %s %s" % (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
  rain = "%s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n" % (r1,r2,r3,r4,r5,r6,r7,r8,r9,r10)
  print(rain, end="")
  r10 = r9
  r9 = r8
  r8 = r7
  r7 = r6
  r6 = r5
  r5 = r4
  r4 = r3
  r3 = r2
  r2 = r1
  time.sleep(1)
