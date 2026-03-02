#to find volume of a cone
import math

# lambda function
volume_cone = lambda r, h: (1/3) * math.pi * r * r * h

# example
r = 3
h = 5
print("Volume =", volume_cone(r, h))