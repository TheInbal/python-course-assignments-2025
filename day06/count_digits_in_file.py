from collections import Counter

# Path to the input and output files
input_file = "C:\Inbal/University/Chemistry Msc Weizmann/Courses/Python Course/day06/numbers.txt"
output_file = "report.txt"

# Counter for digits
digit_counter = Counter()

# Read the file and count digits
with open(input_file, "r") as f:
    for line in f:
        for char in line:
            if char.isdigit():
                digit_counter[char] += 1

# Write the results to report.txt
with open(output_file, "w") as report:
    for digit in sorted(digit_counter.keys()):
        report.write(f"{digit}: {digit_counter[digit]}\n")

print(f"Digit counts have been written to {output_file}")
