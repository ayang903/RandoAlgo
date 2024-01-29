import networkx as nx
import random
from collections import defaultdict

def get_edge_list(G):
    return tuple(sorted(tuple(sorted(e)) for e in G.edges()))

N = 100000

# store frequency of each MST
mst_counts = defaultdict(int)

for _ in range(N):
    # complete graph with 6 vertices
    G = nx.complete_graph(6)

    # G = nx.Graph()
    # G.add_nodes_from([1, 2, 3, 4])
    # G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

    # Assign random edge weights from [0, 1]
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.uniform(0, 1)

    # find the minimum spanning tree using networkx
    mst = nx.minimum_spanning_tree(G)

    # put the edges in a standard, sorted, format
    mst_edge_list = get_edge_list(mst)

    # Increment the count
    mst_counts[mst_edge_list] += 1

# sort the MSTs by count, divide most frequent by N to get probability
sorted_msts = sorted(mst_counts.items(), key=lambda x: x[1], reverse=True)
most_frequent_mst, highest_count = sorted_msts[0]
probability = highest_count / N

print(f"Most Frequent MST: {most_frequent_mst}, Count: {highest_count}")
print(f"Probability of this MST: {probability}")

unif = 1 / len(sorted_msts) # n^(n-2) after many trials
print(f"Uniform distribution would give probability {unif}")

