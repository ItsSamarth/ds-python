# CREATE CLASS
class MyClass:
    x=5

# CREATE OBJECT
obj= MyClass()
print(obj.x)


#__init__() all classes have a function to assign values to object property
#or other operations that are necessary to do when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " +  self.name)

p1 = Person("samarth", 23) #__init__()  function is called automatically when the object is created

print(p1.name)
print(p1.age)
p1.myfunc()

#delete object property

del p1.age

#delete object
del p1
