import pandas as pd
from sqlalchemy import create_engine

# Step 1: Set PostgreSQL credentials
DB_USERNAME = 'cristy'  # Replace with your username
DB_PASSWORD = 'Indica182'  # Replace with your PostgreSQL password
DB_HOST = 'localhost'  # Database host, usually localhost
DB_PORT = '5432'  # Default PostgreSQL port
DB_NAME = 'mlb_stats'  # Name of the database

# Create the database connection string
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Step 2: Read the CSV file into a DataFrame
csv_file = 'mlb_batting_stats_2024.csv'  # Replace with the correct filename
print(f"Reading data from {csv_file}...")
data = pd.read_csv(csv_file)

# Step 3: Clean the DataFrame
# Remove unsupported data types for PostgreSQL
print("Cleaning data to ensure compatibility with PostgreSQL...")
cleaned_data = data.select_dtypes(include=['number', 'object']).copy()

# Rename columns to make them PostgreSQL-compatible
cleaned_data.columns = [col.replace(" ", "_").lower() for col in cleaned_data.columns]
print(f"Columns after cleaning: {list(cleaned_data.columns)}")

# Step 4: Connect to the PostgreSQL database
print("Connecting to the database...")
engine = create_engine(DATABASE_URL)

# Step 5: Load the cleaned data into the database
try:
    print("Loading data into the player_stats table...")
    cleaned_data.to_sql('player_stats', con=engine, if_exists='replace', index=False)
    print("Data loaded successfully into the 'player_stats' table!")
except Exception as e:
    print(f"An error occurred: {e}")