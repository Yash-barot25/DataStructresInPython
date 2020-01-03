cars = {"Lambo": "A glamorous look with power",
        "Tesla": "A very first driver less electrical car",
        "Bugatti": "A very high speed car of the century",
        "Maserati": "A luxuries car"}
print(type(cars))
# print(cars)
# print(cars["Lambo"])
# cars["Lambo"] = "Also a great looking car"
# print(cars["Lambo"])
# print(cars)
# del cars["Lambo"]
# del cars
# cars.clear()
# print(cars)
# print(cars["honda"])
# while True:
#     dict_key = input("Enter a key\n")
#     if dict_key.upper() == "QUIT":
#         break
#     if dict_key in cars:
#         dict_value = cars.get(dict_key)
#         print(dict_value)
#     else:
#         print("We don't have " + dict_key)
# while True:
#     dict_key = input("Enter a key\n")
#     if dict_key.upper() == "QUIT":
#         break
#     print(cars.get(dict_key, "We don't have a " + dict_key))
# cars = {"Lambo": "A glamorous look with power",
#         "Tesla": "A very first driver less electrical car",
#         "Bugatti": "A very high speed car of the century",
#         "Maserati": "A luxuries car"}

# values = cars.values()
# print(values)
#
# keys = cars.keys()
# print(keys)
# for f in keys:
#     print(cars[f])

# has_key a deprecated function of python 2
for f in cars:
    print(cars[f])


list_keys = list(cars.keys())
print(list_keys)

list_keys.sort()
for k in list_keys:
    print(cars[k])


