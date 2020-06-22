class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#特殊的属性，放在方法里，作为私有的属性，经过调用才可以用
    def set_att(self,value):
        self.value="fit"

    def eat(self):
        print(f"name:{self.name}),age:{self.age},gender:{self.gender}我在吃.")
    def drink(self):
        print(f"name:{self.name}),age:{self.age},gender:{self.gender}我在喝.")
    def run(self):
        print(f"name:{self.name}),age:{self.age},gender:{self.gender}我在跑.")

xiaoming=Person("xiaoming", 10, 'male')
xiaohong=Person("xiaohong", 15, 'famale')

print(xiaoming.name)
xiaoming.run()

xiaoming.set_att("fit")
print(xiaoming.value)
