# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Test single line comment

"""
Test multi-line comment
this is multi-line comment
"""

MyName = "Test Name"
print(MyName)

IsOK = True
StateOK = "I am OK"
StateNotReady = "I am not ready"
if IsOK :
    print(StateOK)
else :
    print(StateNotReady)


aValue, bValue = 0, 1

if aValue < bValue and aValue == 0:
    print(aValue)
elif aValue == 1:
    print("aValue == 1 %d", aValue)
elif 0 < aValue < 1:
    print("0 < aValue < 1 %d", aValue)
else:
    print(bValue)

loopTime = 10
while loopTime > 0:
    if loopTime == 2:
        print("stop loop %d", loopTime)
        break;
    print("loop %d", loopTime)
    loopTime -= 1
else:
    print("loop end")

loopTime = 10
while loopTime > 0:
    loopTime -= 1
    if loopTime == 2:
        print("special loop %d", loopTime)
        continue;
    print("loop %d", loopTime)
else:
    print("loop end")


strTest = "testspring"

for i in strTest :
    print("cur char is %c", i)
else:
    print("for end")

numSerials = (0, 1, 2, 3, 4, 5)
for i in numSerials:
    print("cur num is %d", i)
else:
    print("for end")

print(type(numSerials))

listMixData = [2, "word", 3.1, True, "word"]

print(type(listMixData))

for i in listMixData:
    print("cur num is %d", i)

print("word pos in listMixData is %d", listMixData.index("word", 0, 3))
print("word count in listMixData is %d", listMixData.count("word"))
print("listMixData len is %d", len(listMixData))

print("word" in listMixData)
print("Word" in listMixData)

print("word" not in listMixData)
print("Word" not in listMixData)

resultOne = 1 / 2
print("resultOne is %d", resultOne)
resultTwo = 1 // 2
print("resultTwo is %d", resultTwo)

nameList = ("jack", "tom", "bot")
nameOnlyList = ("jack", )
print(type(nameOnlyList))

nameOnly = ("jack")
print(type(nameOnly))

dict1 = {'name': 'tom', 'age': 18}
print(type(dict1))
print(dict1['name'])

dict2 = {}

dict3 = dict()


set1 = {0, 1, 2, 3, 4}
print(set1)

set2 = set("abcdefg")
print(set2)

set3 = {0, 0, 0, 1}
print(set3)

setEmpty = set()
print(setEmpty)

def test_func(a, b):
    c = a + b
    print("test func %d", c)


test_func(10, 20)

func2 = lambda : 100

print(func2)
print(func2())

func3 = lambda a, b=1: a + b
print(func3(20))
print(func3(20, 30))

class classA():
    def printInfo(self):
        print("this is class A")

objA = classA()
objA.printInfo()

class classBase(object):
    name = "classBase"
    __innername = "__innerclassBase"
    def __print_innername(self):
        print(self.__innername)
    def __init__(self, width, height):
        self.name = "Myname"
        self.width = width
        self.height = height
    def __str__(self):
        print("this is class Base, my name is %s", self.name)
        return self.name
    def __del__(self):
        print("del %s", self.name)
    @staticmethod
    def printStaticInfo():
        print("this is the static method of classBase")

    def printInfo(self):
        print("this is class Base")
        print("my name is %s", self.name)
        self.__print_innername()

class classB(classBase):
    pass

objB = classBase(5500, 800)
objB.printInfo()

class classBase2(object):
    def printInfo(self):
        print("this is class Base2")
    def printInfo2(self):
        print("this is class Base2")

class classC(classBase, classBase2):
    pass

objC = classC(500, 800)
objC.printInfo2()
print(classBase.name)
objB.name = "classB"
print(objB.name)
objC.name = "classC"
print(objC.name)

print(objC)

classBase.printStaticInfo()
objB.printStaticInfo()

del  objC

try:
    print(objC)
except Exception as result:
    print(result)
else:
    print("ok")
finally:
    print("just do it")


import random, math
random.uniform(10.0, 20.0)
math.acos(1.0)


print('''line1
line2
line3''')

baseValue = 2
powerValue = 10
print(baseValue**powerValue)


x = float(input("x:"))
y = float(input("y:"))
print("x * y = ", x * y)


