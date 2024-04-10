import pandas as pd
import networkx as nx

# 读取用户互动数据
user_interactions_df = pd.read_csv('cleaned_item_share_train_info.csv')

# 读取用户信息数据
user_info_df = pd.read_csv('cleaned_user_info.csv')

# 创建网络
user_interaction_graph = nx.Graph()

# 添加节点和属性
for index, row in user_info_df.iterrows():
    user_interaction_graph.add_node(row['user_id'], gender=row['user_gender'], age=row['user_age'], level=row['user_level'])

# 添加边
for index, row in user_interactions_df.iterrows():
    # 确保只添加图中已存在的用户节点之间的边
    if row['inviter_id'] in user_interaction_graph and row['voter_id'] in user_interaction_graph:
        user_interaction_graph.add_edge(row['inviter_id'], row['voter_id'])

# 输出网络信息
print(f"Number of nodes: {user_interaction_graph.number_of_nodes()}")
print(f"Number of edges: {user_interaction_graph.number_of_edges()}")

# 保存网络到文件
nx.write_gexf(user_interaction_graph, 'whole_user_interaction_network.gexf')

# 输出完成信息
print("Network created and saved as GEXF.")
