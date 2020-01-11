def dfs(graph, start):
    """
    Search a graph statring from a given element using DFS.
    :param geaph: graph to be searched.
    :param srart: starting node of search-path.
    :return: list of nodes representing the path taken in the search.
    """
    path = []
    q = [start]
    while q:
        v = q[0]
        q = q[1:]
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print(dfs(graph, 'A'))
