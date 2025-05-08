from itertools import permutations

def tsp(graph, start=0):
    n = len(graph)
    vertices = list(range(n))
    min_path = float('inf')
    for perm in permutations(vertices):
        if perm[0] != start:
            continue
        cost = 0
        for i in range(n - 1):
            cost += graph[perm[i]][perm[i+1]]
        cost += graph[perm[-1]][perm[0]]
        min_path = min(min_path, cost)
    return min_path

graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

print("Minimum cost:", tsp(graph))
