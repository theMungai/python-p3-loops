#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
print(happy_new_year())


def square_integers(int_list):
    square = [integer ** 2 for integer in int_list]
    return square
print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    i = 1
    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
fizzbuzz()
