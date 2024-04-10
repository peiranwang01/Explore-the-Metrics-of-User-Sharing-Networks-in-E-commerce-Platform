import matplotlib.pyplot as plt
import networkx as nx
import matplotlib

# Load the graph with community information
G = nx.read_gexf('user_interaction_network_with_communities.gexf')

# Extract community information from each node
communities = [data['community'] for node, data in G.nodes(data=True)]

# Create a color map for the communities
unique_communities = set(communities)
cmap = matplotlib.cm.get_cmap('viridis', len(unique_communities))
node_color = [cmap(community) for community in communities]

# Draw the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=20)
plt.title('Community structure')
plt.axis('off')

# Save the plot to a PNG file
plt.savefig('community_structure.png', format='PNG', dpi=300)

# Show the plot
plt.show()
