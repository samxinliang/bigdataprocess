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

        
    
