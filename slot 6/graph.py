# class Node:
#     def __init__(self, x):
#         self.node = x
#     adjNode = []

#     def addNode(self, x):
#         self.adjNode.append(x)

#     def dfs(self, flag, trail, end):
#         if(self.node == end): 
#             print(trail)
#             return 
        
#         for x in self.adjNode:
#             if(x in flag and flag[x] == 1): continue
#             tmpflag = [x for x in flag]
#             tmptrail = [x for x in trail]
#             flag[x] = 1
#             trail.append(x)
#             nodeList[x].dfs(flag, trail, end)
#             flag = tmpflag
#             trail = tmptrail
#             flag[x] = 0
        

# nodeList = {}
# numNode = int(input('Nhap so dinh: '))
# for i in range(numNode):
#     node = input('Nhap dinh: ')
#     nodeList[node] = Node(node)

# numEdge = int(input('Nhap so canh: '))
# for i in range(numEdge):
#     x, y = input('Nhap 2 dinh cua canh: ').split()
#     nodeList[x].addNode(y)

# x = input('Nhap dinh xuat phat: ')
# y = input('Nhap dinh dich: ')

# flag = {x: 1}
# trail = [x]

# nodeList[x].dfs(flag, trail, y)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = {} 

def dfs(visited, graph, node, end, trail):  #function for dfs 
    if node in visited and visited[node] == 1: return
    tmp = [x for x in trail] 
    tmp.append(node)

    if(node == end):
        print(tmp)
        return

    visited[node] = 1
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour, end, tmp)
    visited[node] = 0


# Driver Code
dfs(visited, graph, '5', '8', [])

    