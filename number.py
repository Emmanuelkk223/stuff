try:
    x = int(input("What's x? "))
except ValueError:
    print(f"x is not a number")
    exit()
print(f"x is {x}")
