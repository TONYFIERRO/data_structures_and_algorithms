import itertools
import random
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
import math

# Initial vertex
INITIAL_VERTEX = 1

# Way
S = np.array([INITIAL_VERTEX - 1])

# Amount of vertex on the graph
K = 6

# Weights
WEIGHT = np.array([[0, 19, 41, 39, 27, 20],
                   [19, 0, 24, 31, 35, 13],
                   [41, 24, 0, 20, 41, 22],
                   [39, 31, 20, 0, 26, 20],
                   [27, 35, 41, 26, 0, 23],
                   [20, 13, 22, 20, 23, 0]])

# Tau coefficient
TAU = np.array([[0, 1, 2, 2, 2, 3],
                [1, 0, 1, 1, 1, 1],
                [2, 1, 0, 3, 2, 3],
                [2, 1, 3, 0, 1, 3],
                [2, 1, 2, 1, 0, 2],
                [3, 1, 3, 3, 2, 0]], dtype='f')

# Amount of iterations
AMOUNT_OF_ITERATIONS = 1500

# Alpha
ALPHA = 1

# Beta
BETA = 1

# Q coefficient
Q = 4

# p coefficient
p = 0.32

# Optimal way and optimal length
optimal_L = math.inf
optimal_S = None

for current_iteration in range(AMOUNT_OF_ITERATIONS):
    for subiteration in range(K - 1):
        list_of_P = list()
        last_index_of_S = len(S) - 1
        for way in range(K):
            if way not in S:
                P_a = ((1 / WEIGHT[S[last_index_of_S]][way]) ** BETA * (TAU[S[last_index_of_S]][way] ** ALPHA))
                P_b = 0
                for i in range(K):
                    if i is not S[last_index_of_S] and i not in S:
                        P_b += ((1 / WEIGHT[S[last_index_of_S]][i]) ** BETA) * ((TAU[S[last_index_of_S]][i]) ** ALPHA)

                if P_a != 0 and P_b != 0:
                    P = 100 * (P_a / P_b)
                    if len(list_of_P) > 0:
                        list_of_P.append([math.ceil(list_of_P[-1][0] + P), way])
                    else:
                        list_of_P.append([math.ceil(P), way])

        # print(list_of_P)

        random_digit = random.randint(1, 100)
        # print(random_digit)
        for i in range(len(list_of_P)):
            if random_digit <= list_of_P[i][0]:
                S = np.append(S, list_of_P[i][1])
                break

    S = np.append(S, INITIAL_VERTEX - 1)
    # print(S)
    L = 0
    for i in range(1, len(S)):
        L += WEIGHT[S[i - 1]][S[i]]
    # print(L)

    if L < optimal_L:
        optimal_L = L
        optimal_S = S

    for i in range(K):
        for j in range(K):
            if i != j:
                TAU[i][j] = (1 - p) * TAU[i][j]
                TAU[i][j] = (1 - p) * TAU[i][j]
    for i in range(1, len(S)):
        TAU[S[i - 1]][S[i]] += Q / L

    S = np.array([INITIAL_VERTEX - 1])

optimal_S = [elem + 1 for elem in optimal_S]

print(f'Optimal way: {optimal_S}')
print(f'Optimal length: {optimal_L}')

# Create a graph
graph = nx.Graph()
nodes = range(1, K + 1)
pairs = itertools.permutations(nodes, 2)
graph.add_nodes_from(nodes)
graph.add_edges_from(pairs)
nx.draw_networkx(graph, node_color='black', font_color='white', node_size=750, with_labels=True)
man = plt.get_current_fig_manager()
man.set_window_title("Graph: Ant Colony Optimization Algorithm")
plt.show()
