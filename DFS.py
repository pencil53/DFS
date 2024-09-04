def add_edge(adj,s,t):
    #add edge from vertex s to t
    adj[s].append(t)
    #due to undirected graph
    adj[t].append(s)

def dfs_rec(adj,visited,s):
    #mark the current vertex as visited
    visited[s] = True

    #print the current vertex
    print(s,end=" ")

    #recursibely visit all adjacent nodes that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj,visited,i)

def dfs(adj,s):
    visited = [False] * len(adj)
    dfs_rec(adj,visited,s)

if __name__=="__main__":
    V= 5

    #create a adjency list for the graph
    adj = [[] for _ in range(V)]

    #define the edges of the graph
    edges = [[1,2],[1,0],[2,0],[2,3],[2,4]]

    #populate the adjency list with edges
    for e in edges:
        add_edge(adj,e[0],e[1])

        source = 1
        print("DFS from source: ",source)
        dfs(adj,source)