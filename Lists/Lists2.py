numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
another_numbers = numbers

numbers.sort(reverse=True)
print(another_numbers)
print(numbers is another_numbers)
print(numbers == another_numbers)
another_numbers = list(numbers)
another_numbers.sort()
print(numbers is another_numbers)
print(numbers == another_numbers)
print(list("hello yash here"))

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
numbers_list = [odd, even]
print(numbers_list)
for numberset in numbers_list:
    print(numberset)
    for num in numberset:
        print(num)
        
