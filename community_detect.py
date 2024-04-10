import numpy as np
import pandas as pd
import networkx as nx
from community import community_louvain
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 载入数据
users_df = pd.read_csv('cleaned_user_info.csv')
shares_df = pd.read_csv('cleaned_item_share_train_info.csv')

# 构建图
G = nx.Graph()

# 添加节点
for _, user in users_df.iterrows():
    G.add_node(user['user_id'], gender=user['user_gender'], age=user['user_age'], level=user['user_level'])

# 添加边
for _, share in shares_df.iterrows():
    G.add_edge(share['inviter_id'], share['voter_id'])

# 社区检测
partition = community_louvain.best_partition(G)
# 保存图G
nx.write_gexf(G, "network_graph.gexf")

# 分析每个社区的特性
community_info = {}
for user, comm in partition.items():
    if comm not in community_info:
        community_info[comm] = {'users': [], 'ages': [], 'levels': [], 'genders': []}
    community_info[comm]['users'].append(user)
    community_info[comm]['ages'].append(users_df.loc[users_df['user_id'] == user, 'user_age'].values[0])
    community_info[comm]['levels'].append(users_df.loc[users_df['user_id'] == user, 'user_level'].values[0])
    community_info[comm]['genders'].append(users_df.loc[users_df['user_id'] == user, 'user_gender'].values[0])

# 基于Louvain算法分配的社区信息，计算图中每个节点的社区归属
for node in G.nodes:
    G.nodes[node]['community'] = partition[node]

# 计算每个社区的颜色
unique_communities = list(set(partition.values()))
colors = cm.rainbow(np.linspace(0, 1, len(unique_communities)))
community_colors = {comm: colors[i] for i, comm in enumerate(unique_communities)}

# 可视化
plt.figure(figsize=(14, 9))
# 使用更快的布局算法
pos = nx.kamada_kawai_layout(G)

# 画出节点
for community in unique_communities:
    node_list = [node for node in partition if partition[node] == community]
    node_color = [community_colors[community]] * len(node_list)
    nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_color=node_color, label=str(community))

# 画出边
nx.draw_networkx_edges(G, pos, alpha=0.5)

# 添加标签
nx.draw_networkx_labels(G, pos, font_size=8)

# 添加图例
plt.legend(scatterpoints=1)

# 显示图
plt.title('Community Structure Visualization')
plt.axis('off')

# 保存生成的图像
plt.savefig("community_structure.png", format="PNG")

plt.show()
