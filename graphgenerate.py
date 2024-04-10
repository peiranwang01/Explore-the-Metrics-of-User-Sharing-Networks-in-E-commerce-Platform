import networkx as nx
from community import community_louvain
import pandas as pd

# 载入数据（省略了数据加载代码）

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

# 将社区信息添加到节点属性中
for node, comm_id in partition.items():
    G.nodes[node]['community'] = comm_id

# 分析每个社区的特性并添加到节点属性中
for node, comm_id in partition.items():
    # 这里仅示范添加了社区ID，您可以根据需要添加其他社区特性
    user_info = users_df.loc[users_df['user_id'] == node]
    if not user_info.empty:
        G.nodes[node]['age'] = user_info['user_age'].values[0]
        G.nodes[node]['level'] = user_info['user_level'].values[0]
        G.nodes[node]['gender'] = user_info['user_gender'].values[0]

# 保存带有社区信息的图G为GEXF格式
nx.write_gexf(G, "network_with_communities.gexf")
print: '保存成功'
