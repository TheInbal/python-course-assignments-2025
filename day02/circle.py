import numpy as np

radius = input("Please enter circle radius (write numbers only):")
radius = float(radius)
area = np.pi * (radius) ** 2
circumeference = 2 * np.pi * radius

print(f"Area: {area}, circumeference: {circumeference}")