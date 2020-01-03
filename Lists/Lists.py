cities = ["mississauga", "brampton", "oakville", "scarborough", "ajex"]
print(cities)
print(sorted(cities))
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
print(odd + even)
numbers = odd + even
numbers.sort()
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

if numbers == (odd+even):
    print("Lists are equal")
else:
    print("Lists are not equal")

if numbers == sorted_numbers:
    print("Lists are equal")
else:
    print("Lists are not equal")
