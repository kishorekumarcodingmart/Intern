nodes = []

graph = []

node_count = 0

def add_node(node):
    global node_count
    if node in nodes:
        print(node," is allready present in thr graph")
    else:
        node_count+=1
        nodes.append(node)
        for col in graph:
            col.append(0)
        temp = []
        for row in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(node1,node2): 
    if node1 not in nodes:
        print(node1," is not present in the graph")
    elif node2 not in node2:
        print(node2," is not present in the graph")
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = 1

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")

add_edge("A","B")
add_edge("A","C")

print_graph()  