# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
n1 = random.randint(1,100)
n2 = random.randint(1,100)
while True:
    solution = n1 + n2
    answer = eval(input('%d + %d = '%(n1, n2)))
    if answer == solution:
        print('Correct,you are very good.')
        break
    else:
        print('Wrong answer,try again.')
print('Over')

total = 0
number = 1
while number <= 15:
    if number % 5 == 0:
        number += 1
        continue
    print('%3d'%(number),end = '  ')
    total += number
    number += 1
    
print('\ntotal = %d'%(total))
