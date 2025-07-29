test = input()
print(test)

elements = test.split()

print()
print(test)

bool_checks = [el.isdigit() for el in elements]
print(bool_checks)
print(bool_checks[0])
print(bool_checks[1])
