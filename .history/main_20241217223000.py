from pybaseball import batting_stats
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Fetch Batting Stats
year = int(input("What year do you want to collect batting stats for?: "))

print(f"Fetching batting stats for the {year} season...")
data = batting_stats(year)

# Step 2: Clean DataFrame
# Remove columns that are unsupported in PostgreSQL (e.g., complex data types)
print("Cleaning data to ensure compatibility with PostgreSQL...")
cleaned_data = data.select_dtypes(include=['number', 'object']).copy()

# Optionally, rename columns to remove spaces or special characters
cleaned_data.columns = [col.replace(" ", "_").lower() for col in cleaned_data.columns]

# Save to a CSV file
file_name = f"mlb_batting_stats_{year}.csv"
cleaned_data.to_csv(file_name, index=False)
print(f"Data saved to {file_name}")

# Step 3: Database Connection Configuration
DB_USERNAME = 'postgres'  # Replace with your PostgreSQL username
DB_PASSWORD = 'your_password'  # Replace with your PostgreSQL password
DB_HOST = 'localhost'  # Default is localhost
DB_PORT = '5432'  # Default PostgreSQL port
DB_NAME = 'mlb_stats'  # Replace with your database name

# Create the database connection string
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Step 4: Connect to the Database
print("Connecting to the PostgreSQL database...")
engine = create_engine(DATABASE_URL)

# Step 5: Load Data into the Database
try:
    print("Loading data into the player_stats table...")
    cleaned_data.to_sql('player_stats', con=engine, if_exists='replace', index=False)
    print("Data loaded successfully into the 'player_stats' table!")
except Exception as e:
    print(f"An error occurred: {e}")