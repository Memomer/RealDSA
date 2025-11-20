def adjacency_list_dictionary(V, edges):

    adjacency_list = {}

    for i in range(V):
        adjacency_list[i] = []

    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_list[vertex1].append(vertex2)

    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex} -> {''.join(map(str, neighbors))}")

