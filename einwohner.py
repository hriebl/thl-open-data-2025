from urllib.error import URLError

import altair as alt
import pandas as pd
import streamlit as st


@st.cache_data
def get_data():
    df = pd.read_csv(
        "https://opendata.luebeck.de/bereich/1.102/statistik/bevoelkerung/"
        "einwohner-stadtteile/einwohner-stadtteile.csv",
        sep=";",
    )

    df = df.set_index("stadtteil_name")
    df["stichtag"] = pd.to_datetime(df["stichtag"])
    df["einwohner"] = pd.to_numeric(df["einwohner"])
    return df


try:
    df = get_data()

    stadtteile = st.multiselect(
        label="Wähle Stadtteile",
        options=list(df.index.unique()),
        default=["Innenstadt", "Moisling"],
    )

    if not stadtteile:
        st.error("Wähle mindestens einen Stadtteil")
    else:
        df = df.loc[stadtteile]
        df = df.reset_index()

        chart = (
            alt.Chart(df)
            .mark_point()
            .encode(
                x=alt.X("stichtag", title="Zeitachse"),
                y=alt.Y("einwohner", title="Einwohner"),
                color=alt.Color("stadtteil_name", title="Stadtteil"),
            )
        )

        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(f"Daten konnten nicht geladen werden: {e.reason}")
