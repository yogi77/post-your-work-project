import pandas as pd
import time

# Dictionary to map city names to their respective CSV files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month='all', day='all'):
    """Loads and filters data for the specified city."""
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df = df[df['month'] == months.index(month.lower()) + 1]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...')
    # Extract, find mode, and print common month, day, and hour
    print(f"Most Common Month: {df['month'].mode()[0]}")
    print(f"Most Common Day: {df['day_of_week'].mode()[0]}")
    print(f"Most Common Hour: {df['Start Time'].dt.hour.mode()[0]}")
