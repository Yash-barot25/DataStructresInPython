farm_animals = {"horse", "pig", "hen"}
wild_animals = set(["wolf", "tigers", "lions"])

print(farm_animals)
print(wild_animals)

even = set(range(0, 100, 2))
print(even)
num_squares = (4, 8, 16)
squares = set(num_squares)
print(squares)

print(even.union(num_squares))  # all the values from both sets but not duplicate values
print(even.difference(squares))  # it will remove all element from a first set which are present in 2nd set
print(squares.difference(even))
print(even.intersection(squares))  # it will give a set of common elements present in both sets
# even.intersection_update(squares)
# print(even)
print(even.symmetric_difference(squares))  # it will gives a set of unique values which are not present in both sets

even.remove(20)
# even.remove(25)
even.discard(25)

try:
    even.remove(25)
except KeyError:
    print("A values can't be found")
if even.issuperset(squares):
    print("Even is a super set of a squares")

if squares.issubset(even):
    print("Squared is a sub set of a even")
