try:
    x = int(input("what's x? "))
except ValueError:
    print("x must be an integer")
    exit()

print(f"x is {x}")
