import sys

class Cyclic(Exception):
    pass

def acyclic(adj):

    visited_nodes = [0 for _ in range(len(adj))]
    recur_node_list = [0 for _ in range(len(adj))]

    def dfs(vertex_adj, idx):
        visited_nodes[idx] = 1
        recur_node_list[idx] = 1
        for neighbour in vertex_adj:
            if recur_node_list[neighbour]:
                raise Cyclic
            elif not visited_nodes[neighbour]:
                dfs(adj[neighbour], neighbour)
            
        recur_node_list[idx] = 0
            
    for v in range(len(adj)):
        try:
            if not visited_nodes[v]:
                visited_nodes[v] = 1
                dfs(adj[v], v)
        except Cyclic:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
