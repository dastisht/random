numbers = [77, 46, 11, 89, 48, 14, 67, 73, 22, 26]
sorted_size = 0
size = len(numbers)
while sorted_size < size:
    index = 0
    while index < size - 1 - sorted_size:
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
        index = index + 1
    sorted_size = sorted_size + 1
print(numbers)


