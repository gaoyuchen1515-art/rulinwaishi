import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
import streamlit_folium

# Set page config
st.set_page_config(page_title="The Scholars: Location Analysis (Ch.10-20)", layout="wide")

# 1. Data Preparation
data = {
    "Location": ["Hangzhou", "Yangzhou", "Nanjing", "Suzhou", "Huzhou"],
    "Frequency": [8, 6, 5, 4, 3],
    "Chinese_Name": ["杭州", "揚州", "南京", "蘇州", "湖州"],
    "Latitude": [30.2593, 32.3934, 32.0472, 31.2993, 30.8667],
    "Longitude": [120.1455, 119.4007, 118.7969, 120.6195, 119.9167],
    "Key_Activities": [
        "Ma Chunshang visits West Lake; Kuang Chaoren edits exam papers; poet gatherings",
        "Hu Sandi's poetry events; Niu Buyi's transit; scholar interactions",
        "Niu Puluo's residence; literary exchanges; official transits",
        "Dong Ying's passage; calligraphy/painting exchanges; academic discussions",
        "Lou Brothers' scholar gatherings; Lu Bianxiu's family affairs; Yingtou Lake events"
    ]
}
df = pd.DataFrame(data)

# 2. Title & Introduction
st.title("📜 The Scholars (儒林外史) - Location Analysis (Chapters 10-20)")
st.markdown("""
This visualization analyzes **5 key locations** from Chapters 10-20, comparing their appearance frequency and related scholar activities. 
Insights: Hangzhou and Yangzhou are core hubs for scholars (examination, poetry, social interaction), reflecting the Ming Dynasty's literary culture and regional mobility.
""")

# 3. Frequency Bar Chart
st.subheader("📊 Appearance Frequency of Locations")
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']  # Support Chinese
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["Chinese_Name"], df["Frequency"], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
ax.set_xlabel("Location (地點)", fontsize=12)
ax.set_ylabel("Frequency (出現次數)", fontsize=12)
ax.set_title("Location Frequency in Chapters 10-20", fontsize=14, fontweight='bold')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{int(height)}', ha='center', va='bottom', fontsize=11)
st.pyplot(fig)

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle
import numpy as np

# 数据准备
data = {
    "Location": ["Hangzhou", "Yangzhou", "Nanjing", "Suzhou", "Huzhou"],
    "Frequency": [8, 6, 5, 4, 3],
    "Chinese_Name": ["杭州", "揚州", "南京", "蘇州", "湖州"],
    "Latitude": [30.2593, 32.3934, 32.0472, 31.2993, 30.8667],
    "Longitude": [120.1455, 119.4007, 118.7969, 120.6195, 119.9167],
    "Key_Activities": [
        "Ma Chunshang visits West Lake; Kuang Chaoren edits exam papers; poet gatherings",
        "Hu Sandi's poetry events; Niu Buyi's transit; scholar interactions",
        "Niu Puluo's residence; literary exchanges; official transits",
        "Dong Ying's passage; calligraphy/painting exchanges; academic discussions",
        "Lou Brothers' scholar gatherings; Lu Bianxiu's family affairs; Yingtou Lake events"
    ]
}
df = pd.DataFrame(data)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制地图背景（这里简化为空白，实际可叠加地图底图）
ax.set_xlim(118, 121)
ax.set_ylim(30, 33)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("The Scholars: Location Frequency (Ch.10-20)")

# 定义颜色和大小映射
colors = {8: 'red', 6: 'orange', 5: 'blue', 4: 'green', 3: 'purple'}
sizes = df['Frequency'] * 20

# 绘制散点
scatter = ax.scatter(
    df['Longitude'], 
    df['Latitude'], 
    s=sizes, 
    c=[colors[val] for val in df['Frequency']],
    alpha=0.7
)

# 添加标签和图例
for i, txt in enumerate(df['Chinese_Name']):
    ax.text(df['Longitude'][i] + 0.05, df['Latitude'][i] + 0.05, txt, fontsize=10)

# 自定义图例（频率与颜色、大小的对应）
legend_elements = [
    Circle((0, 0), radius=8, color='red', label='Frequency: 8'),
    Circle((0, 0), radius=6, color='orange', label='Frequency: 6'),
    Circle((0, 0), radius=5, color='blue', label='Frequency: 5'),
    Circle((0, 0), radius=4, color='green', label='Frequency: 4'),
    Circle((0, 0), radius=3, color='purple', label='Frequency: 3')
]
ax.legend(handles=legend_elements, title="Frequency Legend", loc='upper right')

# 显示图形
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 在Streamlit中展示（若需要）
# import streamlit as st
# st.pyplot(fig)

# 5. Detailed Activity Comparison
st.subheader("📋 Key Activities by Location")
st.dataframe(df[["Chinese_Name", "Frequency", "Key_Activities"]], use_container_width=True)

# 6. Insights Summary
st.subheader("💡 Core Insights")
st.markdown("""
1. **Hangzhou (杭州)** (8 times): The most active location, linking examination culture (Ma Chunshang, Kuang Chaoren editing papers) and literary gatherings—reflecting its status as a cultural center in the Ming Dynasty.
2. **Yangzhou (揚州)** (6 times): A transit hub for scholars and officials, with activities like poetry events (Hu Sandi) and transits (Niu Buyi)—showing its role in regional mobility.
3. **Scholar Mobility**: Locations like Nanjing, Suzhou, and Huzhou are connected by scholar interactions (e.g., Lou Brothers' gatherings, Dong Ying's transit), highlighting the network of literati across the Jiangnan region.
4. **Social Context**: Activities (examination preparation, poetry recitals, marriage arrangements) mirror the Ming scholars' focus on imperial examinations, social status, and cultural exchanges.
""")
