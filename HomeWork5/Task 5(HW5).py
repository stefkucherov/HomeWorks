from functools import reduce


def calculate_area(room):
    return room["length"] * room["width"]


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

areas = list(map(calculate_area, rooms))

total_area = reduce(lambda x, y: x + y, areas)
print('Площадь квартиры = ', total_area)
