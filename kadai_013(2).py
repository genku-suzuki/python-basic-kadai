import random
from random import randint, randrange
price = randint(1,10000)
print("消費税抜き"+str(price)+"円の商品は消費税込みの場合")
def calculate_total(price):
  total = price + price *0.1
  print(f"{total}円です")
calculate_total(price)