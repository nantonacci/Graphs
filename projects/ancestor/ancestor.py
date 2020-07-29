from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        g.add_edge(i[1], i[0])

    q = Queue()
    q.enqueue([starting_node])

    max_path = 1
    earliest = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        for next_item in g.vertices[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest