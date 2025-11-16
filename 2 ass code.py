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

# 数据准备（地点名称改为英文）
data = {
    "Location": ["Hangzhou", "Yangzhou", "Nanjing", "Suzhou", "Huzhou"],
    "Frequency": [8, 6, 5, 4, 3],
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
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(df["Location"], df["Frequency"], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
ax.set_xlabel("Location", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
ax.set_title("Location Frequency in Chapters 10-20", fontsize=14, fontweight='bold')

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{int(height)}', ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.show()

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
