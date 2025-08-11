#Class & objects 
# class MyClass:
#     x=23
# p = MyClass()
# print(p.x)

# __init__ __str__ 

# class Person:
#      def __init__(alamin,name):
#         alamin.name = name
        
#      def getName(alamin):
#       return alamin.name
        
# p = Person('kabir')
# p.name = "asik"
# print(p.getName())


# =====================
# __str__  = control data represention
# __init_  = setup data
class Person:
     def __init__(alamin,name,age):
        alamin.name = str(name)
        alamin.age = int(age)
        
     def __str__(alamin):
       return f"{alamin.name}({alamin.age})"
        
p = Person("alamin",23.3)
print(p)




 
 
 
 
