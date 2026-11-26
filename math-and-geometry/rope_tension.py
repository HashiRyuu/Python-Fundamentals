MASS = 2
R = 3
MAX_TENSION = 60

v = int(input("Enter the rotation speed: "))
tension = (MASS * v**2) / R

if tension > MAX_TENSION:
    print("The rope breaks.")
else :
    print("The rope does not break.")
