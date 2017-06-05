"""
Given a graph, represented as a dictionary of lists, find all paths between the
start and end node. We can solve this problem using DFS or BFS
"""
__author__ = "Gary Tang"


def get_all_paths(start, end, graph):
    """
    @param start: string or int representing the starting node in the the graph
    @param end: string or int representing the ending node in the the graph
    @param graph: dictionary of lists
    @return paths: list of list of paths between start and end
    """
    paths = []

    def valid_path(start, end, path=[]):
        """Helper function that recursively traverses the adjacent nodes"""
        if start in path:
            # found a cycle
            return []
        path = path + [start]
        if start == end:
            # base case
            return path
        elif not graph[start]:
            # node does not point to other nodes
            return []
        else:
            for node in graph[start]:
                update_path = valid_path(node, end, path)
                if update_path:
                    paths.append(update_path)  # end of path
    valid_path(start, end)
    return paths


# test cases
g = {'A': ['B', 'C'],
     'B': ['C']}
assert(get_all_paths('A', 'C', g) == [['A', 'B', 'C'], ['A', 'C']])

g = {0: [1],
     1: [2],
     2: [0, 3],
     3: [2]}
assert(get_all_paths(0, 3, g) == [[0, 1, 2, 3]])

g = {'A': ['B', 'C'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C'],
     'E': ['F'],
     'F': ['C']}
assert(get_all_paths('A', 'D', g) == [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']])
