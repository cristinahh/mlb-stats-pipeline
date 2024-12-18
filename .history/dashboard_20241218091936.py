import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# Database connection
DB_USERNAME = 'cristy'
DB_PASSWORD = 'Indica182'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'mlb_stats'
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL)

# Streamlit app
st.title("MLB Player Stats Dashboard")

# Query data
query = """
SELECT name, team, home_runs, batting_avg, games_played
FROM player_stats
ORDER BY home_runs DESC
LIMIT 10;
"""
data = pd.read_sql(query, con=engine)

# Display data
st.header("Top 10 Players by Home Runs")
st.table(data)

# Add a chart
st.bar_chart(data.set_index("name")["home_runs"])