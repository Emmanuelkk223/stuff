def main():
    name = "Hello world"
    capital(name)

def capital(name):
    for i in name:
        if i.islower():
            print(i.upper(), end="")
        else:
            print(i, end="")
main()
