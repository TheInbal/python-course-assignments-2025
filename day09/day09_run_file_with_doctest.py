import day09_module
import sys

numbers = sys.argv[1]


digit_count_dict = day09_module.count_digits_in_numbers(numbers)
day09_module.print_digit_counts(digit_count_dict)