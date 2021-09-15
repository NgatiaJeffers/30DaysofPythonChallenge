# Iterate 0 to 10
count = 0
while count < 10:
    print(count)
    count = count + 1
    if count == 10:
        break

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# Iterate 10 to 0
count = 10
while count > 0:
    print(count)
    count = count - 1
    if count == 0:
        break

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for number in numbers:
    print(number)
