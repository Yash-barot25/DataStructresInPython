text = input("Enter something:\n").upper()
# text_char = list(text)
# consonants = set()
#
# for i in text:
#     if i not in 'AEIOU ':
#         consonants.add(i)
# print(sorted(text_char))
# print(sorted(consonants))

# set_value = set("a", "e", "i", "o", "u")
set_value = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U", " "}
input_text = set(text)

final_set = input_text.difference(set_value)
print(final_set)
