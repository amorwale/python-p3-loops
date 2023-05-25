#!/usr/bin/env python3

def happy_new_year():
    x = 10
    while x > 0:
        print(x)
        x -= 1
    print('Happy New Year!')
    pass
    

def square_integers(int_list):
    int_list = [int * int for int in int_list]
    return int_list
    

def fizzbuzz():
    x = 1
    while x <= 100:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz") 
        elif x % 3 == 0:
            print("Fizz") 
        elif x % 5 == 0:
            print("Buzz") 
        else: print(x) 
        x += 1
    pass
