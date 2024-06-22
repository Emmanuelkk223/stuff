def convert(f):
    return round((f - 32) * 5 / 9)

temps = {
    "Karachi": 86,
    "London": 65,
    "New York": 56,
    "Tokyo": 70
}

for city in temps:
    if convert(temps[city]) > 20:
        print(city)
