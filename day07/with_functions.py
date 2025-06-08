def digits_count_dict_creation():
    return {str(d): 0 for d in range(10)}

def count_digits_in_numbers(numbers):
    digit_count = digits_count_dict_creation()
    for number in numbers:
        for digit in str(abs(number)):
            digit_count[digit] += 1
    return digit_count

def print_digit_counts(digit_count):
    for digit in sorted(digit_count.keys(), key=int):
        print(f"{digit}  {digit_count[digit]}")

if __name__ == "__main__":
    numbers = [1203, 1256, 312456, 98]
    digit_count_dict = count_digits_in_numbers(numbers)
    print_digit_counts(digit_count_dict)
