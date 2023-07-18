import random

var = random.randint(0,1000)

if var % 3 == 0 and var % 5 == 0:
 print(var,"FizzBuzz")
elif var % 3 == 0:
 print(var,"Fizz")
elif var % 5 == 0:
 print(var,"Buzz")
else:
 print(var)