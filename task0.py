def find(numbers):
    list_of_numbers = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            list_of_numbers.append(numbers[i])
    return list_of_numbers

numbers = input("Введите список: ").split()
numbers = [int(x) for x in numbers]
result = find(numbers)
print(result)