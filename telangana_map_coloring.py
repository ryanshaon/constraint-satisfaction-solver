"""Telangana map coloring using CSP backtracking plus graph visualization."""

import matplotlib.pyplot as plt
import networkx as nx

DISTRICTS = [
    "Adilabad",
    "Nizamabad",
    "Karimnagar",
    "Warangal",
    "Khammam",
    "Nalgonda",
    "Mahbubnagar",
    "Hyderabad",
]
COLORS = ["Red", "Green", "Blue"]
NEIGHBORS = {
    "Adilabad": ["Nizamabad", "Karimnagar"],
    "Nizamabad": ["Adilabad", "Karimnagar", "Hyderabad"],
    "Karimnagar": ["Adilabad", "Nizamabad", "Warangal"],
    "Warangal": ["Karimnagar", "Khammam", "Nalgonda"],
    "Khammam": ["Warangal", "Nalgonda"],
    "Nalgonda": ["Warangal", "Khammam", "Hyderabad", "Mahbubnagar"],
    "Mahbubnagar": ["Nalgonda", "Hyderabad"],
    "Hyderabad": ["Nizamabad", "Nalgonda", "Mahbubnagar"],
}


def is_valid(district, color, assignment):
    for neighbor in NEIGHBORS[district]:
        if assignment.get(neighbor) == color:
            return False
    return True


def choose_unassigned_district(assignment):
    for district in DISTRICTS:
        if district not in assignment:
            return district
    return None


def backtrack(assignment):
    if len(assignment) == len(DISTRICTS):
        return dict(assignment)

    district = choose_unassigned_district(assignment)
    if district is None:
        return None

    for color in COLORS:
        if not is_valid(district, color, assignment):
            continue

        assignment[district] = color
        result = backtrack(assignment)
        if result:
            return result
        del assignment[district]

    return None


def build_graph():
    graph = nx.Graph()
    for district, district_neighbors in NEIGHBORS.items():
        for neighbor in district_neighbors:
            graph.add_edge(district, neighbor)
    return graph


def main():
    solution = backtrack({})

    print("Solution:")
    for district in DISTRICTS:
        print(f"{district} = {solution[district]}")

    graph = build_graph()
    color_map = [solution[node].lower() for node in graph.nodes()]

    plt.figure(figsize=(8, 6))
    positions = nx.spring_layout(graph)
    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_color=color_map,
        node_size=2000,
        font_size=8,
    )

    plt.title("Telangana Map Coloring (CSP Visualization)")
    plt.show()


if __name__ == "__main__":
    main()