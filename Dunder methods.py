#they are special methods- start and end with double underscores
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"hello how are you and your name is {self.name}"
    def __add__(self,other):
        sum =0
        for i in other:
            sum=sum+i.age
        return f"sum of ages are {self.age + sum}"

obj=Animal("Amit",12)
obj2=Animal("cow",15)
obj3=Animal("tiger",13)
print(obj +(obj2 ,obj3))