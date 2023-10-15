def count_duplicates(strings):
    counts = {}
    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    return counts.values()
strings = input("Введите строки: ").split()
print(*count_duplicates(strings))