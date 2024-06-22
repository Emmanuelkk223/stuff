def main():
    int_num = int(input("Number: "))
    int_num_factorial = f(int_num)
    print(f"{int_num}! = {int_num_factorial}")


def f(n):
    if n < 0:
        raise ValueError()
    elif n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)
    
main()
