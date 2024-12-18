from pybaseball import batting_stats
import pandas as pd

year = int(input("What year do you want to collect batting stats for?:"))

# Fetch batting stats for the 2023 season
print(f"Fetching batting stats for the {year} season...")
data = batting_stats(year)

# Save to a CSV file
file_name = f"mlb_batting_stats_{year}.csv"
data.to_csv(file_name, index=False)
print(f"Data saved to {file_name}")