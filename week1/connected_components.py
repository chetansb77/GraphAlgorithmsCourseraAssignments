import sys

def number_of_components(adj):

    components_count = 0
    identified_node_list = []

    def dfs(vertex_adj):
        for neighbour in vertex_adj:
            if neighbour not in identified_node_list:
                identified_node_list.append(neighbour)
                dfs(adj[neighbour])
        
        return

    for i in range(len(adj)):
        if i not in identified_node_list:
            dfs(adj[i])
            components_count = components_count + 1

    return components_count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
