

def count_digits_in_numbers(numbers):
    """ 
    Counts the appearance of each digit (0-9) in a list of numbers.

    :Param numbers: a list of integers that are being checked.
    :type numbers: list of int

    :return: a dictionary mapping the counts of each digit.
    :rtype: dict 

    Example:
    >>> count_digits_in_numbers([1203, -45])
    {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 0, '7': 0, '8': 0, '9': 0}
    """
    digit_count = {str(d): 0 for d in range(10)}
    for number in numbers:
        for digit in str(abs(number)):
            digit_count[digit] += 1
    return digit_count

def print_digit_counts(digit_count):
    for digit in sorted(digit_count.keys(), key=int):
        print(f"{digit}  {digit_count[digit]}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
