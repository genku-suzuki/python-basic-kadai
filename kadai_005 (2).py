#台形の面積を計算する公式
def trapezoid(x,y,z):
  return int((x+y)*z/2)

#台形の上辺と下辺と高さを設定
top_side=10
bottom_side=20
height=5

#台形の面積を計算する関数を呼び戻して戻り値をareaとする
area=trapezoid(top_side,bottom_side,height)

print("台形の面積は"+str(area)+"㎠です。")