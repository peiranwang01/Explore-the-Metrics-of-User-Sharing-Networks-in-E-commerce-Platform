import pandas as pd

# 加载数据
df = pd.read_csv('clean_item_info_for_use.csv')

# 计算 'cate_level1_id' 列的种类数量
num_categories = df['brand_id'].nunique()

# 打印结果
print(f"种类数量（brand_id）: {num_categories}")
