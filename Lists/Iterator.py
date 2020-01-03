string = "123456789"
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for number in string:
    print(number, end="")

numbers = iter(string)
day = iter(days)
print()
for i in range(0, len(string)):
    print(next(numbers), end="")

print()
for i in range(0, len(days)):
    print(next(day), end=" ")