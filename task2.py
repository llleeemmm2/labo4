def count_numbers(list1, list2):
    common_numbers = set(list1) & set(list2)
    return len(common_numbers)

list1 = input("Введите первый список: ").split()
list1 = [int(x) for x in list1]
list2 = input("Введите второй список: ").split()
list2 = [int(x) for x in list2]
result = count_numbers(list1, list2)
print(result)