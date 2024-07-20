fees = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

input_fees = int(input("Fees: "))
allow = []
not_allowed = []

for x in fees:
    if input_fees < 500:
        allow.append(x)
    else:
        not_allowed.append(x)
if input_fees in allow:
    print("\nAllow")
elif input_fees in not_allowed:
    print("\nNot Allowed")

