import random
from random import randint, randrange
price = randint(1,10000)
tax = price*0.1
print("消費税抜き"+str(price)+"円の商品は消費税込みの場合")
def add_two_arguments(price,tax):
  total = price + tax
  print(f"{total}円です")
add_two_arguments(price,tax)