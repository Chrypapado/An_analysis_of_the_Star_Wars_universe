# Function to find the most connected nodes within a partition
def community_name(G, node_to_partition_id, partition_id):
    
    nodes_in_partition = [node for node in G.nodes() 
                          if node_to_partition_id[node] == partition_id]
    sub_G = G.subgraph(nodes_in_partition)
    node_to_connectivity = [(node, sub_G.degree(node)) for node in sub_G.nodes()]
    top_node = sorted(node_to_connectivity, key=lambda t: t[1], reverse=True)[:1]
    return top_node