import math

MM_PER_INCH = 25.4
LETTER_M = 8.5
LETTER_N = 11

Perimeter = 2*(LETTER_M + LETTER_N)
Diagonal = math.sqrt(LETTER_M**2 + LETTER_N**2)

print("The perimeter is", Perimeter, "inches.")
print("The length of the diagonal is", Diagonal, "inches.")
