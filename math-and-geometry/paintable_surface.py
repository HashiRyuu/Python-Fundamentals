HOUSE_WIDTH = 23
HOUSE_LENGTH = 45
HOUSE_HEIGHT = 9.5

WINDOW_N = 12
WINDOW_WIDTH = 3
WINDOW_HEIGHT = 3.5

DOOR_N = 4
DOOR_WIDTH = 3
DOOR_HEIGHT = 7.5

houseAreaSurface = 2 * (HOUSE_WIDTH * HOUSE_HEIGHT) + 2 * (HOUSE_LENGTH * HOUSE_HEIGHT)
windowAreaTotal = (WINDOW_WIDTH * WINDOW_HEIGHT) * WINDOW_N
doorAreaTotal = (DOOR_WIDTH * DOOR_HEIGHT) * DOOR_N

paintableArea = houseAreaSurface - windowAreaTotal - doorAreaTotal

print("The surface area to be painted of a house is %.2f sqft." % paintableArea)
