import matplotlib.pyplot as plt
import networkx as nx

# Create a new graph
G = nx.Graph()

# Define nodes
core_switches = ["core1", "core2", "core3", "core4"]
aggregation_switches = [
    "aggr1",
    "aggr2",
    "aggr3",
    "aggr4",
    "aggr5",
    "aggr6",
    "aggr7",
    "aggr8",
]
edge_switches = ["edge1", "edge2", "edge3", "edge4", "edge5", "edge6", "edge7", "edge8"]
hosts = [
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "h7",
    "h8",
    "h9",
    "h10",
    "h11",
    "h12",
    "h13",
    "h14",
    "h15",
    "h16",
]

# Add nodes
G.add_nodes_from(core_switches, layer="core")
G.add_nodes_from(aggregation_switches, layer="aggregation")
G.add_nodes_from(edge_switches, layer="edge")
G.add_nodes_from(hosts, layer="host")

# Add edges from configuration
links = [
    ("h1", "edge1"),
    ("h2", "edge1"),
    ("h3", "edge2"),
    ("h4", "edge2"),
    ("h5", "edge3"),
    ("h6", "edge3"),
    ("h7", "edge4"),
    ("h8", "edge4"),
    ("h9", "edge5"),
    ("h10", "edge5"),
    ("h11", "edge6"),
    ("h12", "edge6"),
    ("h13", "edge7"),
    ("h14", "edge7"),
    ("h15", "edge8"),
    ("h16", "edge8"),
    ("edge1", "aggr1"),
    ("edge1", "aggr2"),
    ("edge2", "aggr1"),
    ("edge2", "aggr2"),
    ("edge3", "aggr3"),
    ("edge3", "aggr4"),
    ("edge4", "aggr3"),
    ("edge4", "aggr4"),
    ("edge5", "aggr5"),
    ("edge5", "aggr6"),
    ("edge6", "aggr5"),
    ("edge6", "aggr6"),
    ("edge7", "aggr7"),
    ("edge7", "aggr8"),
    ("edge8", "aggr7"),
    ("edge8", "aggr8"),
    ("aggr1", "core1"),
    ("aggr1", "core2"),
    ("aggr2", "core3"),
    ("aggr2", "core4"),
    ("aggr3", "core1"),
    ("aggr3", "core2"),
    ("aggr4", "core3"),
    ("aggr4", "core4"),
    ("aggr5", "core1"),
    ("aggr5", "core2"),
    ("aggr6", "core3"),
    ("aggr6", "core4"),
    ("aggr7", "core1"),
    ("aggr7", "core2"),
    ("aggr8", "core3"),
    ("aggr8", "core4"),
]
G.add_edges_from(links)

# Define node positions for symmetry
pos = {}

# Set core switch positions with core2 and core3 aligned to the middle
pos["core1"] = (-4.5, 3)
pos["core2"] = (-1.5, 3)
pos["core3"] = (1.5, 3)
pos["core4"] = (4.5, 3)

# Set aggregation switch positions
for i in range(len(aggregation_switches)):
    pos[aggregation_switches[i]] = ((i - 3.5) * 3, 2)

# Set edge switch positions
for i in range(len(edge_switches)):
    pos[edge_switches[i]] = ((i - 3.5) * 3, 1)

# Set host positions with h8 and h9 aligned to the middle
for i in range(len(hosts)):
    if hosts[i] == "h8":
        pos[hosts[i]] = (-1.25, 0)
    elif hosts[i] == "h9":
        pos[hosts[i]] = (1.25, 0)
    else:
        pos[hosts[i]] = ((i - 7.5) * 2.5, 0)

# Define Morandi colors
morandi_colors = {
    "core": "#8E8D8A",
    "aggregation": "#CFC4B2",
    "edge": "#A3C6C4",
    "host": "#D3E0DC",
}

# Draw the graph with different colors for each layer
plt.figure(figsize=(18, 14))

node_color_map = []
node_size_map = []
for node in G:
    if node in core_switches:
        node_color_map.append(morandi_colors["core"])
        node_size_map.append(4500)  # Core node size
    elif node in aggregation_switches:
        node_color_map.append(morandi_colors["aggregation"])
        node_size_map.append(4500)  # Aggregation node size
    elif node in edge_switches:
        node_color_map.append(morandi_colors["edge"])
        node_size_map.append(4500)  # Edge node size
    elif node in hosts:
        node_color_map.append(morandi_colors["host"])
        node_size_map.append(3000)  # Host node size (smaller)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_size_map,
    node_color=node_color_map,
    font_size=14,
    font_weight="bold",
    edge_color="brown",
)
plt.title("k=4 Fat Tree Topology", size=20)
plt.savefig("fat_tree_topology.png")
plt.show()
