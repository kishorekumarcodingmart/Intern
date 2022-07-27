graph = {}


def add_node(node):
    if node in graph:
        print(node," is already present in graph")
    else:
        graph[node] = []

def add_edge(node1,node2):
    if node1 not in graph:
        print(node1," is not present in the graph")
    elif node2 not in graph:
        print(node2," is not present in the graph")
    else:
        graph[node1].append(node2)

def print_graph():
    for i in graph:
        print(i, graph[i])

add_node("A")
add_node("B")
add_node("C")

add_edge("A","B")
add_edge("B","C")
add_edge("A","C")


print_graph()