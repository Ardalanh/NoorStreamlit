import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
import graphs

st.set_page_config(layout="wide")
st.title("User bahaviour Analysis")


DATA_TAB, ENAGED_TAB, DIST_TAB = st.tabs(["Data", "Engaged", "Column Distributions"])




def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df
    orig_df = df
    df = orig_df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    return df
df = pd.read_csv("D:\\Noor\\Data\\Processed\\BehaviourData_Users_Cluster.csv")


with ENAGED_TAB:

    df_filter = filter_dataframe(df)

    # Data frame showing
    total_users = df.shape[0]
    df['Engaged'] = df.index.to_series().apply(lambda x: 1 if x in set(df_filter.index) else 0)

    st.write(f"You selected {df['Engaged'].sum()} users out of {total_users} users.")

    st.dataframe(df_filter, height=300)

    draw_graphs_button = st.button("Draw")

    if df['Engaged'].sum() != 0 and df['Engaged'].sum() != total_users and draw_graphs_button:
        with st.expander("Session"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.session_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.session_graphs(df, "Engaged", stat="probability", common_norm=False))


        with st.expander("Session Gaps"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.session_gaps_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.session_gaps_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Session Nums"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.session_nums_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.session_nums_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Game Behaviour"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.game_behaviour_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.game_behaviour_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Levels"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.levels_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.levels_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Rv Interstitial"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.rv_interstitial_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.rv_interstitial_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Interstitial Placement"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.interstitial_placements_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.interstitial_placements_graphs(df, "Engaged", stat="probability", common_norm=False))

        with st.expander("Totals"):
            count_tab, nomalized_tab = st.tabs(["Count", "Normalized"])
            with count_tab:
                st.pyplot(graphs.totals_graphs(df, "Engaged"))

            with nomalized_tab:
                st.pyplot(graphs.totals_graphs(df, "Engaged", stat="probability", common_norm=False))

DATA_PATH = Path.cwd()/Path("Visualization")

with DATA_TAB:
    sections = ["Session",  "Session Gaps", "Session Nums", "Game Behaviour",
                "Levels", "Rv Interstitial", "Interstitial Placement", "Totals"]
    for section in sections:
        with st.expander(section):
            full_tab, cohort_tab, nomalized_tab = st.tabs(["Full", "Cohort", "Cohort Normalized"])
            section_name = section.replace(" ", "_")
            with full_tab:
                st.image(Image.open(DATA_PATH/f"{section_name}.png"))
            with cohort_tab:
                st.image(Image.open(DATA_PATH/f"{section_name}_Cohort.png"))
            with nomalized_tab:
                st.image(Image.open(DATA_PATH/f"{section_name}_Cohort_Normal.png"))


with DIST_TAB:
    PERCENTILES = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
    st.dataframe(df.drop("devtodev_ID", axis=1).describe(PERCENTILES), height=457)
