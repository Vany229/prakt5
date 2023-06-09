array = [2, -3, 5, 7, -4, 0, 8, -1, 6]
sum_positive = 0
count_positive = 0
product_negative = 1
for element in array:
    if element > 0:
        sum_positive += element
        count_positive += 1
    elif element < 0:
        product_negative *= element
average_positive = sum_positive / count_positive
print("Среднее арифметическое положительных элементов:", average_positive)
print("Произведение отрицательных элементов:", product_negative)