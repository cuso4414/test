class C:
    #类的属性
    cc = 10

    print("类的静态属性",C.cc)

    a = C()
    b = C()
    print("实例对象a",a.cc)
    print("实例对象b",b.cc)
    b.cc = 20
    print("第二次，类的静态属性",C.cc)
    print("第二次，实例属性a", a.cc)
    print("第二次，实例属性b", b.cc)
    C.cc = 30
    print("第二次，类的静态属性", C.cc)
    print("第二次，实例属性a", a.cc)
    print("第二次，实例属性b", b.cc)