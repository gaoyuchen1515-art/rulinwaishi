import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# Page config
st.set_page_config(page_title="The Scholar - Chapters 20-30", layout="wide")

# Title
st.title("Location Frequencies in *The Scholar* (Chapters 20-30)")
st.markdown("Geospatial Visualization of Place Mentions & Character Activities")

# Actual data from Chapters 20-30 (close reading results)
# Format: [Place, Latitude, Longitude, Frequency, Key Characters, Core Activities]
location_data = [
    ["Nanjing (南京)", 32.0603, 118.7969, 8, "Quan San, Kuang Chaoren", "Legal disputes, marriage arrangements, official document processing"],
    ["Yangzhou (揚州)", 32.3932, 119.4989, 6, "Niu Buyi, Kuang Chaoren", "Scholar gatherings, poetry exchanges, transit for imperial examinations"],
    ["Suzhou (蘇州)", 31.2993, 120.6195, 5, "Dong Ying, Kuang Chaoren", "Waiting for official appointments, literary interactions with gentry"],
    ["Wuhu (蕪湖)", 31.3597, 118.3874, 4, "Niu Buyi, Niu Pulang", "Temporary residence for scholars, poetry creation, identity fraud"],
    ["Hangzhou (杭州)", 30.2741, 120.1551, 3, "Jing Lanjiang, Zhao Xuezhai", "Poetry clubs, academic discussions, examination preparation"],
    ["Zhejiang Leqing (浙江樂清)", 28.1443, 120.9438, 3, "Kuang Chaoren, Kuang Da", "Family affairs, ancestral burial, return for examinations"],
    ["Shaoxing (紹興)", 29.9902, 120.5853, 2, "Kuang Chaoren, Li Jijiu", "Imperial examination fraud, academic fraud"],
    ["Nanjing Yanziji (南京燕子磯)", 32.1408, 118.9337, 1, "Kuang Chaoren", "Transit hub for river travel"]
]

# Create DataFrame
df = pd.DataFrame(
    location_data,
    columns=["Place", "Latitude", "Longitude", "Frequency", "Key Characters", "Core Activities"]
)

# Base map (focused on Eastern China)
m = folium.Map(location=[31.5908, 119.7895], zoom_start=7, tiles="CartoDB positron")

# Add interactive markers (size proportional to frequency)
for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=row["Frequency"] * 2,  # Scale for visibility
        color="#2E86AB",
        fill=True,
        fill_color="#A23B72",
        fill_opacity=0.8,
        popup=folium.Popup(f"""
        <strong>{row['Place']}</strong><br>
        Frequency: {row['Frequency']} mentions<br>
        Key Characters: {row['Key Characters']}<br>
        Activities: {row['Core Activities']}
        """, max_width=350)
    ).add_to(m)

# Display map
st.subheader("Geospatial Distribution of Locations (Chapters 20-30)")
folium_static(m, width=1100, height=600)

# Key insights from close reading
st.subheader("Critical Insights from Chapters 20-30")
st.write("""
1. **Nanjing’s Central Role**: As the former imperial capital, Nanjing dominates with 8 mentions, serving as a hub for legal matters (Quan San’s lawsuits), social mobility (Kuang Chaoren’s marriage), and bureaucratic processes. It reflects the novel’s critique of official corruption and academic fraud.

2. **Yangzhou-Suzhou Cultural Axis**: These Jiangnan cities (6 and 5 mentions) remain key for scholar interactions—Yangzhou hosts poetry gatherings and exam transit, while Suzhou is tied to official appointments. They highlight the region’s enduring status as a literary and political nexus.

3. **Wuhu’s Narrative Significance**: Though mentioned 4 times, Wuhu is pivotal for character development—Niu Buyi’s death and Niu Pulang’s identity theft occur here, symbolizing the erosion of scholarly integrity.

4. **Regional Focus Shift**: Unlike earlier chapters, Chapters 20-30 expand beyond major cities to include smaller locales (e.g., Leqing, Shaoxing), linking rural scholar life to urban power dynamics. Kuang Chaoren’s journey from Leqing to Nanjing mirrors his moral decline from filial son to corrupt opportunist.

5. **Activity Differentiation**: Political/legal activities cluster in Nanjing, cultural exchanges in Yangzhou/Hangzhou, and personal moral conflicts in Wuhu/Leqing—showing how locations shape character behavior and thematic exploration.
""")

# Raw data table
st.subheader("Detailed Frequency & Activity Data")
st.dataframe(df[["Place", "Frequency", "Key Characters", "Core Activities"]], use_container_width=True)
