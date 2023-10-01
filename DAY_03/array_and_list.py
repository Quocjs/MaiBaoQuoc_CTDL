array = [10, 3, 7, 5]

#ví dụ 1:
print(array[0])

#ví dụ 2:
print(array[:])

#ví dụ 3:
print(array[0:3])

#ví dụ 4:
max = array[0]

for num in array:
    if num > max:
        max = num
print(f"Giá trị lớn nhất trong mảng là {max}")

min = array[0]
for num in array:
    if num < max:
        min = num
print(f"Giá trị nhỏ nhất trong mảng là {min}")


