import random
import copy
import numpy as np
import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Temperature
T = 100

# Way
S = np.array([1, 4, 3, 5, 6, 2, 1])

# Amount of vertex
K = len(S) - 1

# Weight of the graph
WEIGHT = np.array([[0, 19, 41, 39, 27, 20],
                   [19, 0, 24, 31, 35, 13],
                   [41, 24, 0, 20, 41, 22],
                   [39, 31, 20, 0, 26, 20],
                   [27, 35, 41, 26, 0, 23],
                   [20, 13, 22, 20, 23, 0]])


# Random number generator
def swapRandomGen():
    rand_a = random.randint(1, K - 1)
    rand_b = random.randint(1, K - 1)
    while rand_a == rand_b:
        rand_b = random.randint(1, K - 1)
    return rand_a, rand_b


# Calculation of the way length
def countL(arr):
    count_L = 0
    for i in range(K):
        count_L += WEIGHT[arr[i] - 1][arr[i + 1] - 1]
    return count_L


amount_of_iterations = 0

while T > 0:
    a, b = swapRandomGen()

    temp_S = copy.deepcopy(S)
    temp_S[a], temp_S[b] = temp_S[b], temp_S[a]
    d_S = countL(temp_S) - countL(S)
    if d_S < 0:
        S = temp_S
    else:
        if (100 * (math.e ** (-d_S / T))) > random.randint(1, 100):
            S = temp_S

    T = float("{0:.6f}".format(0.5 * T))

    amount_of_iterations += 1

print('L =', countL(S))
print('T =', round(T))
print('S =', S)
print(f'Amount of iterations: {amount_of_iterations}')

# Create a graph
graph = nx.Graph()
nodes = range(1, K + 1)
pairs = itertools.permutations(nodes, 2)
graph.add_nodes_from(nodes)
graph.add_edges_from(pairs)
nx.draw_networkx(graph, node_color='black', font_color='white', node_size=750, with_labels=True)
man = plt.get_current_fig_manager()
man.set_window_title("Graph: Simulated Annealing")
plt.show()
