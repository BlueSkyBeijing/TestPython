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
    print("loop %d", loopTime)
    loopTime -= 1

