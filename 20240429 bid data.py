import random
for i in range(1,11):
  ranNum = random.randint(1,100)
  print('%4d' %(ranNum),end = '  ')
  
import random
even = 0
odd = 0
for i in range(1,100):
    randNum = random.randint(1,100)
    print(randNum,end =  '  ')
    if randNum % 2 == 0:
        even += 1
    else:
        odd += 1
print('\neven = %d, odd = %d'%(even,odd))

import random
times3 = 0
times5 = 0
times7 = 0
others = 0
for i in range(1,101):
  flag = False
  randNum = random.randint(1,100)
  print(randNum, end = '  ')
  if randNum % 3 == 0:
    times3 += 1
    flag = True
  if randNum % 5 == 0:
    times5 += 1
    flag = True
  if randNum % 7 == 0:
    times7 +=1
    flag = True
  if flag == False:
    others += 1
print('\ntimes3 = %d, times5 = %d,times7 = %4d'%(times3,times5,times7))
print('other = %d'%(others))

import random
count = 1
while count <= 12:
    for i in range(1,6):
        randNum = random.randint(1,49)
        print('%3d'%(randNum),end = '  ')
    print()
    count += 1
print('over')

import random
again = 1
while again == 1:
    for i in range(1,7):
        randNum = random.randint(1,49)
        print('%3d'%(randNum),end = '  ')
    print()
    again = eval(input('continue:1 or quit:0---->'))
print('Over') 

import random
while True:
    for i in range(1,7):
        randNum = random.randint(1,49)
        print(randNum,end = '  ')
    print()
    if again == 0:
        break
print('over')

    
