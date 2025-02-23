from collections import defaultdict
from pathlib import Path
import sqlite3

import streamlit as st
import altair as alt
import pandas as pd
# import plotly as pt
# import matplotlib as mpt

st.set_page_config(
    page_title="HTC Inventory Tracker",
    page_icon=":package:",
    
)

"""
# :package: Inventory tracker

**Welcome to HTC's Corner Store's intentory tracker!**
This page reads and writes directly from/to our inventory database.

Please remember to update this ASAP when any changes are made.

"""

st.info(
    """
    Use the table below to add, remove, and edit items.
    And don't forget to commit your changes when you're done.
    """
)

st.sidebar.info("Select a demo above.")


options = ["-","Option 1","Option 3"]

selected_option = st.sidebar.selectbox("Choose an option", options)

st.write("You selected: ", selected_option)

