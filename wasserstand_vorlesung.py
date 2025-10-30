import altair as alt
import pandas as pd
import streamlit as st

import folium
from streamlit_folium import st_folium

st.title("Wasserstände Schleswig-Holstein")

st.write(
    """Datenquelle: [Hochwasser-Sturmflut-Information Schleswig-Holstein](https://hsi-sh.de) \\
    Datenherausgeber: [Landesamt für Umwelt Schleswig-Holstein](https://www.schleswig-holstein.de/LFU) \\
    Datenlizenz: [Datenlizenz Deutschland Namensnennung 2.0](https://www.govdata.de/dl-de/by-2-0)"""
)

df = pd.read_csv("https://hsi-sh.de/pegel/od/pegel.csv", sep=";")
# st.dataframe(df)

# center on Liberty Bell, add marker
m = folium.Map(location=[53.8677, 10.68508], zoom_start=12)

for i in range(922):
    folium.Marker(
        [df["geogrBreite"][i], df["geogrLaenge"][i]],
        popup=df["pegelNummer"][i],
        tooltip=df["pegelName"][i],
        icon=folium.Icon()
    ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
popup = st_data["last_object_clicked_popup"]

if popup:
    messwerte = pd.read_csv("https://hsi-sh.de/pegel/download/" + popup + "_Messwerte.csv", sep=";")
    messwerte["Zeit"] = pd.to_datetime(messwerte["Zeit"])

    chart = (
        alt.Chart(messwerte)
        .mark_line()
        .encode(
            x=alt.X("Zeit", title="Zeitachse"),
            y=alt.Y("wasserstand", title="Wasserstand"),
        )
    )

    st.altair_chart(chart, use_container_width=True)
