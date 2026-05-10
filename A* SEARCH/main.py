import heapq

def a_star_search(graph, start, goal, heuristics):
    # priority queue stores (priority, current_node, path, actual_cost)
    pq = [(0 + heuristics[start], start, [start], 0)]
    visited = {}

    while pq:
        f_score, current, path, g_score = heapq.heappop(pq)

        if current == goal:
            return path, g_score

        if current in visited and visited[current] <= g_score:
            continue
        visited[current] = g_score

        for neighbor, cost in graph.get(current, []):
            new_g = g_score + cost
            new_f = new_g + heuristics.get(neighbor, 0)
            heapq.heappush(pq, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')

# Example Usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}
heuristics = {'A': 4, 'B': 2, 'C': 1, 'D': 0}

path, cost = a_star_search(graph, 'A', 'D', heuristics)
print(f"Optimal Path: {path} with cost: {cost}")
