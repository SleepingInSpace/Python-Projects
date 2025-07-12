import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.g_cost = float('inf')  # Cost from start to this node
        self.f_cost = float('inf')  # Total cost (g + h)
        self.parent = None          # For path tracking

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Reverse the path

def a_star_search(graph, start_name, goal_name, heuristics):
    open_set = []
    nodes = {}

    # Initialize the start node
    start_node = Node(start_name, heuristics[start_name])
    start_node.g_cost = 0
    start_node.f_cost = start_node.heuristic
    heapq.heappush(open_set, start_node)
    nodes[start_name] = start_node

    visited = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.name == goal_name:
            return f"Path found: {reconstruct_path(current_node)} with total cost: {current_node.g_cost}"

        visited.add(current_node.name)

        for neighbor_name, cost in graph[current_node.name]:
            if neighbor_name in visited:
                continue

            tentative_g_cost = current_node.g_cost + cost

            # If neighbor is not seen before, create its node
            if neighbor_name not in nodes:
                neighbor_node = Node(neighbor_name, heuristics[neighbor_name])
                nodes[neighbor_name] = neighbor_node
            else:
                neighbor_node = nodes[neighbor_name]

            # Update if this path to neighbor is better
            if tentative_g_cost < neighbor_node.g_cost:
                neighbor_node.g_cost = tentative_g_cost
                neighbor_node.f_cost = tentative_g_cost + neighbor_node.heuristic
                neighbor_node.parent = current_node
                heapq.heappush(open_set, neighbor_node)

    return "Goal not found."

# Example usage
if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("E", 1)],
        "D": [("Goal", 3)],
        "E": [("Goal", 1)],
        "Goal": []
    }

    heuristics = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1,
        "E": 0,
        "Goal": 0
    }

    result = a_star_search(graph, "A", "Goal", heuristics)
    print(result)
