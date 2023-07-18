import random

var = random.randint(0,1000)

print(var)

if var % 3 == 0:
 print(var,"Fizz")
if var % 5 == 0:
 print(var,"Buzz")
elif var % 15 == 0:
 print(var,"FizzBuzz")
else:
 print(var)