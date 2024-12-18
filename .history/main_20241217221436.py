import pandas as pd
from sqlalchemy import create_engine

# Set your PostgreSQL credentials
DB_USERNAME = 'cristy'  # Replace with your username
DB_PASSWORD = 'Indica182'  # Replace with your PostgreSQL password
DB_HOST = 'localhost'  # Database host, usually localhost
DB_PORT = '5432'  # Default PostgreSQL port
DB_NAME = 'mlb_stats'  # Name of the database

# Create the database connection string
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Read the CSV file into a DataFrame
csv_file = 'mlb_batting_stats_2024.csv'  # Replace with the correct filename
print(f"Reading data from {csv_file}...")
data = pd.read_csv(csv_file)

# Connect to the PostgreSQL database
print("Connecting to the database...")
engine = create_engine(DATABASE_URL)

# Load the data into the database
print("Loading data into the player_stats table...")
data.to_sql('player_stats', con=engine, if_exists='replace', index=False)
print("Data loaded successfully!")