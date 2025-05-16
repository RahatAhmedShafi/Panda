# print("Hello Rahat")
# class person:
#     name="Shafi"
#     age=20
# p1=person()
# print(p1.name)

# class fruits:
#     def __init__(self,name,color): #this is a constructor
#         self.name=name
#         self.color=color
#     def welcome(self):
#         print("welcome to the fruit shop")
#     def get_name(self):
#         return self.color
# s1=fruits("apple","red")
# s1.welcome()
# print(s1.name)

# print(s1.get_name())
# class student:
#     def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#     def avg(self):
#         total=0
#         for x in self.marks:
#             total+=x
#         return total/len(self.marks)

# values=[90,80,70]
# s1=student("rahat",values)
# print(s1.avg())


# class person:
#     def __init__(self,name):
#         self.name=name

# values=["rahat","shafi","sakib"]
# s1=person(values)
# print(s1.name)
# del s1.name[0]
# print(s1.name)

               #Inheritance
# class person:
#     feel="good"
#     @staticmethod 

#     def student():
#         v1="ahmed"
#         print("I am a student")
#     @staticmethod
#     def teacher():
#         print("I am a teacher")

# class institute(person):
#     def __init__(self,name):
#         self.name=name

# it1=institute("rahat")
# print(it1.feel)
# print(it1.student())

                       #classmathod
class person:
    name="shafi"
    @classmethod
    def changeName(cls,newName):
        cls.name=newName
cng=person() 
print("Before change: ",cng.name)
cng.changeName("rahat")
print("After change: ",   cng.name)
print("After change: ",person.name)


