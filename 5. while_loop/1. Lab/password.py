user = input()
password = input()
new_try = input()
while new_try != password:
    new_try = input()
print(f"Welcome {user}!")