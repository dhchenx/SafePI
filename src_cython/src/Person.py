#cython: language_level=3

class Person:
    def __init__(self,name="Someone",gender="Unkown",age=25):
        self.name=name
        self.gender=gender
        self.age=age

    def sayHi(self):
        print(f"Hello, I am {self.name}!")

    def sayGoodBye(self):
        print("Bye!")

    def getAge(self):
        return self.age

    def say(self,s):
        print(s)


def greet_and_say(str):
    p=Person()
    p.sayHi()
    p.say(str)






