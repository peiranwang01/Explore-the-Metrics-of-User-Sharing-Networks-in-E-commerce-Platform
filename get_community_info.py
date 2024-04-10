# 初始化社区信息字典
from community_detect import G

community_info = {}

# 遍历图中的每个节点
for node in G.nodes(data=True):
    comm_id = node[1]['community']  # 社区ID
    user_info = {
        'age': node[1]['age'],
        'level': node[1]['level'],
        'gender': node[1]['gender']
    }

    # 如果社区ID在字典中还没有对应的键，创建一个
    if comm_id not in community_info:
        community_info[comm_id] = {
            'users': [],
            'ages': [],
            'levels': [],
            'genders': []
        }

    # 将用户信息添加到社区信息字典中
    community_info[comm_id]['users'].append(node[0])
    community_info[comm_id]['ages'].append(user_info['age'])
    community_info[comm_id]['levels'].append(user_info['level'])
    community_info[comm_id]['genders'].append(user_info['gender'])
