from graph import Graph
def earliest_ancestor(ancestors, starting_node):

    # init graph and add vertices and edges to graph
    gg = Graph()
    for connection in ancestors:
        if connection[0] not in gg.vertices:
            gg.add_vertex(connection[0])
        if connection[1] not in gg.vertices:
            gg.add_vertex(connection[1])
    for connection in ancestors:
        gg.add_edge(connection[1], connection[0])
    result = gg.dfs_ancestor(starting_node)
    if result[-1] == starting_node:
        return -1
    return result[-1]
