graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = {} 

def induongdi(path):
    for u in path[:-1]: 
        print(u, end=' --> ')

    print(path[-1])

def dfs(visited, graph, node, end, trail):  #function for dfs 
    if node in visited and visited[node] == 1: return
    tmp = [x for x in trail] 
    tmp.append(node)

    if(node == end):
        induongdi(tmp)
        return

    visited[node] = 1
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour, end, tmp)
    visited[node] = 0


# Driver Code
start = '5'
end = '8'
print('Cac duong di tu', start, 'den', end, 'la:')
dfs(visited, graph, start, end, [])

    