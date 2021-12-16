import random

# Scouters
S = 10

# The number of bees, which will send to the best places and amount of such places
N = 5
AM_N = 2

# The number of bees, which will send to places near with the best places and amount of such places
M = 2
AM_M = 3

# Place size
D = 10

# Function border by x, y, z
RBORDER = 22
LBORDER = 11

# Amount of iteration
AMOUNT_OF_ITERATIONS = 100000

# Global extremum and coords
GLOBAL_EXTREMUM = [None, None]


# Function
def f(x, y, z):
    # print(x, y, z)
    return -(((x ** 2 + y ** 2) / (x ** 2 - z ** 2 + 1)) * (z + x - y ** 2))
    # Знак минус перед функцией стоит, чтобы найти глобальный максимум


for current_iteration in range(AMOUNT_OF_ITERATIONS):
    storage_of_data = dict()

    for bee in range(S):
        x = random.randint(LBORDER, RBORDER)
        y = random.randint(LBORDER, RBORDER)
        z = random.randint(LBORDER, RBORDER)
        storage_of_data[f(x, y, z)] = [x, y, z]

    N_places = []
    M_places = []
    for i in range(AM_N):
        N_places.append([max(storage_of_data.keys()), storage_of_data[max(storage_of_data.keys())]])
        del storage_of_data[max(storage_of_data.keys())]
    for i in range(AM_M):
        M_places.append([max(storage_of_data.keys()), storage_of_data[max(storage_of_data.keys())]])
        del storage_of_data[max(storage_of_data.keys())]
    # print(N_places)
    # print(M_places)

    storage_of_data = dict()
    for place in N_places:
        for bee in range(N):
            x = random.randint(place[1][0] - D, place[1][0] + D)
            y = random.randint(place[1][1] - D, place[1][1] + D)
            z = random.randint(place[1][2] - D, place[1][2] + D)
            storage_of_data[f(x, y, z)] = [x, y, z]

    for place in M_places:
        for bee in range(M):
            x = random.randint(place[1][0] - D, place[1][0] + D)
            y = random.randint(place[1][1] - D, place[1][1] + D)
            z = random.randint(place[1][2] - D, place[1][2] + D)
            storage_of_data[f(x, y, z)] = [x, y, z]

    if GLOBAL_EXTREMUM[0] == None or GLOBAL_EXTREMUM[0] < max(storage_of_data):
        GLOBAL_EXTREMUM[0] = max(storage_of_data)
        GLOBAL_EXTREMUM[1] = storage_of_data[max(storage_of_data)]
    # for value in storage_of_data:
    #     print(value)
    # print(GLOBAL_EXTREMUM)

print(f'F_MAX = {GLOBAL_EXTREMUM[0]} \nCoords = {GLOBAL_EXTREMUM[1]}')
print(f'Amount of iterations: {AMOUNT_OF_ITERATIONS}')