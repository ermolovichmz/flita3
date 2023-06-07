import graphviz
import networkx

def is_connected(graph):
    num_nodes = len(graph.nodes())
    num_edges = len(graph.edges())
    if num_edges >= ((num_nodes-1)*(num_nodes-2))/2:
        return True
    else:
        return False

graph_data = graphviz.Graph()
graph = networkx.Graph()
with open("text.txt", 'r') as file:
    for line in file:
        vertices = line.strip().split()
        if len(vertices) == 2:
            graph.add_edge(int(vertices[0]), int(vertices[1]))
            graph_data.edge(vertices[0], vertices[1])
        elif len(vertices) == 1:
            graph.add_node(int(vertices[0]))
            graph_data.node(vertices[0])

if is_connected(graph):
    print("Your graph is connected")
else:
    print("Your graph isn't connected")

graph_data.view()
