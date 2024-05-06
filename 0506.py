# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:59:52 2024

@author: C1
"""
for i in range(1,21):
    print('*',end = '  ')
print()

for i in range(1,31):
    print('*',end ='  ')
print()

for i in range(1,51):
    print('*',end = '  ')
print()

def printStar(n):
    for i in range(1,n+1):
        print('*',end = '  ')
    print()
    
def main():
    printStar(20)
    printStar(30)
    printStar(50)
    
main()

def total():
    sum = 0
    for i in range(1,101):
        sum += 1
    print('summation of 1 to 100:',sum)
    
def mian():
    total()
    
main()

def total(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += 1
    return sum 
    sum = 0
    for i in range(a,b+1):
        sum += 1
    return sum 

def main():
    x = eval(input('Enter start number: '))
    y = eval(input('Enter end number:  '))
    t = total(x,y)
    print('summation of %d to %d: %d'%(x,y,t))
    
main()

def total():
    sum = 0
    for i in range(1,101):
        sum += 1
    return sum 

def main():
    t = total()
    print('summation of 1 to 100:',t)
    
main()
