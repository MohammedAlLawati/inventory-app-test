from collections import defaultdict
# from pathlib import path
import sqlite3

import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="HTC Inventory Tracker",
    page_icon=":package:",

)