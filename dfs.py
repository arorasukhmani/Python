adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[]
}

color = {}  # W, G, B
parent = {}
trav_time = {}  # [start, end]
dfs_traversal_output = []

#initialize
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

# print(color)
# print(parent)
# print(trav_time)

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

for u in adj_list.keys():
    if color[u] == "W":
        dfs_util(u)
print(dfs_traversal_output)

print(parent)
print(trav_time)

for node in adj_list.keys():
    print(node," ->", trav_time[node])