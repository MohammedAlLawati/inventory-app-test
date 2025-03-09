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




def connect_db():
    """Connects files to the SQlite Database"""
    DB_FILENAME = Path(__file__).parent / "inventory.db"
    db_already_exists = DB_FILENAME.exists()

    conn = sqlite3.connect(DB_FILENAME)
    db_was_just_created = not db_already_exists

    return conn, db_was_just_created

def initialize_data(conn):
    """initializes initial inventory data, if it has not been created before"""
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            price REAL,
            units_sold INTEGER,
            units_left INTEGER,
            cost_price REAL,
            reorder_point INTEGER,
            description TEXT,
        )
        """
    )


    cursor.execute(
        """
        INSERT INTO inventory
            (item_name, price, units_sold, units_left, cost_price, reorder_point, description)
        VALUES
            ('PV Panels (Jinko)', 1.50, 115, 15, 0.80, 16, 'Hydrating bottled water'),
            ('Soda (355ml)', 2.00, 93, 8, 1.20, 10, 'Carbonated soft drink'),
            ('Energy Drink (250ml)', 2.50, 12, 18, 1.50, 8, 'High-caffeine energy drink')
        """
    )
    conn.commit()

    



