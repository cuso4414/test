class C:
    # 类的属性
    cc = 10

print("类的静态属性", C.cc)
a = C()
b = C()
print("实例对象a", a.cc)
print("实例对象b", b.cc)
b.cc = 20
print("第二次，类的静态属性", C.cc)
print("第二次，实例对象a", a.cc)
print("第二次，实例对象b", b.cc)
C.cc = 30
print("第3次，类的静态属性", C.cc)
print("第3次，实例对象a", a.cc)
print("第3次，实例对象b", b.cc)


class C:
    # 类的属性
    cc = 10
    def method_c(self):
        return "a"

#使用__dict__查看对象的属性
print(C.__dict__)
a = C()
print("第一次打印实例对象属性",a.__dict__)
a.cc = 20
print("第2次打印实例对象属性",a.__dict__)
