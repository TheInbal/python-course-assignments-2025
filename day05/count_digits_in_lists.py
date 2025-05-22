numbers = [1203, 1256, 312456, 98]

digit_count_dict = {}
for digit in range(0, 10):
    digit_count_dict[str(digit)] = 0

    
for number in numbers:
    for digit in str(abs(number)):  
        digit_count_dict[str(digit)] = digit_count_dict[str(digit)] + 1
    

for digit in sorted(digit_count_dict.keys(), key=int):
    print(f"{digit}  {digit_count_dict[digit]}")

