#Creating a class named Person
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    #Implementing a methood called introduce
    def introduce(self):
        print("My name is ",self.name,". I am ",self.age," years old. I am a ",self.gender,".")

#Creating an instance of the class named Person
p1=Person("Eli",19,"Male")

#Calling the introduce method for p1
p1.introduce()