alphabets = "abcdefghijklmnopqrstuvwxyz"

new_string = ""
for letter in alphabets:
    new_string += letter + ", "
print(new_string)

new_string = ", ".join(alphabets)
print(new_string)

