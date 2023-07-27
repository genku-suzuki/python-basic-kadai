class Human:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def check_adult(self):
    print(self.name)
    print(self.age)

    if self.age >= 20:
       print("大人")
    else:
       print("大人ではありません")

human = Human("侍太郎",36)
human.check_adult()