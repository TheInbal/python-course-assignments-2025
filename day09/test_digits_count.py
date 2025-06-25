from day09_module import count_digits_in_numbers


def test_count_digits_in_numbers_basic():
    numbers = [1203, 45]
    expected = {
        '0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1,
        '6': 0, '7': 0, '8': 0, '9': 0
    }
    assert count_digits_in_numbers(numbers) == expected

def test_count_digits_in_numbers_zeros():
    numbers = [0, 100, 2000]
    result = count_digits_in_numbers(numbers)
    assert result['0'] == 6  
    assert result['1'] == 1
    assert result['2'] == 1
