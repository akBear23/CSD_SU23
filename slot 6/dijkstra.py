from queue import PriorityQueue

trace = []

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        trace[neighbor] = current_vertex
    return D

def rollback(trace, start, end):
    if(start != end and trace[end] == -1): return('Khong co duong di')
    path = []
    while(end != -1):
        path.append(end)
        end = trace[end]
    x = path.reverse()
    return path

# vertices = int(input('Nhap so dinh: '))
# edges = int(input('Nhap so canh: '))

# g = Graph(9)
# for i in edges:
#     x = input('Nhap dinh thu nhat: ')
#     y = input('Nhap dinh thu hai: ')
#     w = int(input('Nhap trong so cua canh: '))
#     g.add_edge(x, y, w)

# start = input('Nhap dinh xuat phat: ')
# end = input('Nhap dinh dich: ')

# D = dijkstra(g, 0)
# print(D[end])

g = Graph(9)
trace = [-1 for i in range(9)]
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3) 

D = dijkstra(g, 0)
end = 3
path = rollback(trace, 0, 3)
print('Do dai duong di ngan nhat den dinh',end,'la',D[end])
print('Duong di ngan nhat la: ')
for u in path[:-1]: 
    print(u, end=' --> ')

print(path[-1])