min_length = 2

while True:
    name = input('Please enter your name: ')
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break

print(f"Hello, {name}")
