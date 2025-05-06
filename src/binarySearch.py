def binary_search(number_list, number_to_find):
    low = 0
    high = len(number_list) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if number_list[mid] == number_to_find:
            return f"Number found in index: {mid}\nTotal Number of keys examined: {count}"
        elif number_list[mid] < number_to_find:
            low = mid + 1
        else:
            high = mid - 1

    return f"Number not found\nTotal Number of keys examined: {count}"

# Ejemplos de uso
if __name__ == "__main__":
    number_list = [10, 11, 12, 16, 18, 23, 29, 33, 48, 54, 57, 68, 77, 84, 98]
    number_to_find = 48
    print(binary_search(number_list, number_to_find))