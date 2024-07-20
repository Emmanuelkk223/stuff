items = ["biscuit", "monkey", True, False, 223, 88, 77, 88.98]
string = []
boolean = []
number = []
floats = []

for item in items:
    if type(item) == str:
        string.append(item)
    elif type(item) == bool:
        boolean.append(item)
    elif type(item) == int:
        number.append(item)
    elif type(item) == float:
        floats.append(item)

print(string)

print(boolean)

print(floats)

print(number)
