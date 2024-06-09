def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid_index1 = n // 2 - 1
        mid_index2 = n // 2
        median = (sorted_numbers[mid_index1] + sorted_numbers[mid_index2]) / 2
    else:
        mid_index = n // 2
        median = sorted_numbers[mid_index]
    return median
numbers = [5, 2, 8, 1, 6, 4]
median = find_median(numbers)
print("Median:", median)
