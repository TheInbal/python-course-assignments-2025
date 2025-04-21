import numpy as np
import sys

radius = float(sys.argv[1])
area = np.pi * (radius) ** 2
circumference = 2 * np.pi * radius

print(f"Area: {area}, circumference: {circumference}")