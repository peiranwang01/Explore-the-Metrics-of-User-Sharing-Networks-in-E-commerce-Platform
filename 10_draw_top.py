import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
import numpy as np
from collections import Counter
import colorsys

# Load the graph with community information
G = nx.read_gexf('user_interaction_network_with_communities.gexf')

# Extract community information from each node
communities = [data['community'] for node, data in G.nodes(data=True)]
community_size = Counter(communities)

# Filter communities by size > 200
large_communities = {community for community, size in community_size.items() if size > 200}

# Create subgraph containing only large communities
large_community_nodes = [node for node, data in G.nodes(data=True) if data['community'] in large_communities]
subG = G.subgraph(large_community_nodes)

# Create a color map for the communities in the subgraph
unique_communities_subG = set([data['community'] for node, data in subG.nodes(data=True)])
cmap = matplotlib.colormaps['viridis']
colors = cmap(np.linspace(0, 1, len(unique_communities_subG)))
community_colors = {comm: colors[i] for i, comm in enumerate(unique_communities_subG)}
node_color_subG = [community_colors[data['community']] for node, data in subG.nodes(data=True)]


# 通过调整颜色的亮度和饱和度来增强颜色的区分度
def adjust_color(color, brightness_factor=1.2, saturation_factor=1.2):
    r, g, b, alpha = matplotlib.colors.to_rgba(color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0, min(1, l * brightness_factor))
    s = max(0, min(1, s * saturation_factor))
    new_r, new_g, new_b = colorsys.hls_to_rgb(h, l, s)
    return new_r, new_g, new_b, alpha

# 使用调整后的颜色
community_colors = {comm: adjust_color(colors[i]) for i, comm in enumerate(unique_communities_subG)}

# Draw the subgraph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(subG, seed=42)  # For consistent layout
nx.draw_networkx_edges(subG, pos, alpha=0.5)
nx.draw_networkx_nodes(subG, pos, node_color=node_color_subG, node_size=20)
plt.title('Community structure (size > 500)')
plt.axis('off')

# Save the plot to a PNG file
plt.savefig('large500_community_structure.png', format='PNG', dpi=300)

# Show the plot
plt.show()
