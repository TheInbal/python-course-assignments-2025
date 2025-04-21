import sys

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
perimeter = (2 * height) + (2 * width)

print(f"Rectangle area: {area}, rectangle perimeter: {perimeter}")