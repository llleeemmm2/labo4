def swap_numbers(numbers):
    if len(numbers) < 2:
        return list

    min_index = 0
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
        if numbers[i] > numbers[max_index]:
            max_index = i

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers

numbers = input("Введите список: ").split()
numbers = [int(x) for x in numbers]
result = swap_numbers(numbers)
print(result)
