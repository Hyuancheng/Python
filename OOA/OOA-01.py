'''
关于类与对象,需要明确四个元素,即:
一.类
二.类的成员
三.对象.
四.对象的成员
类与对象的关系,有以下几个特点:
1.当类被赋值给对象的时候,会为对象创建一个空的类,对象的成员实际上仍指向对它赋值的类,即对象成员地址与类成员的地址相同;
2.当对象中某一成员被重新赋值时,对象的空壳中会添加一个新成员,因此该新成员与类中相同成员拥有不同的地址;
3.无论是修改类还是对象中的成员,都无法改变类和对象的地址.
'''
class B():
    name = "shuaige"
    age = 23

a = B()
print(id(a))
#验证1 新创建一个空的类
print(B.__dict__)
print(a.__dict__)

print("*" * 20)

#验证1 对象成员与类成员地址相同
print(B.name)
print(id(B.name))
print(a.name)
print(id(a.name))

print("*" * 20)

#验证2 对象成员被重新赋值,对象中新增成员,成员地址发生改变
a.name = "meinv"
print(a.name)
print(a.__dict__)
print(id(a.name))

print("*" * 20)

#验证3 修改类和对象中的成员,仅改变成员地址,不改变类和对象的地址
print("a的id为",":",id(a))
print(id(B))
print(id(B.name))
B.name = "goudan"
print(id(B))
print(id(B.name))
