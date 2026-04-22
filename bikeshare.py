import pandas as pd
import time

# Dictionary to map city names to their respective CSV files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print("Hello! Let's explore some US bikeshare data!")

    # City Input
    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid city name. Please try again.")

    # Month Input
    while True:
        month = input("Enter month (all, january, february, ... june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        print("Invalid month. Please enter a month from January to June or 'all'.")

    # Day Input
    while True:
        day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        print("Invalid day. Please try again.")

    print('-' * 40)
    return city, month, day

def load_data(city, month='all', day='all'):
    """Loads and filters data for the specified city."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df = df[df['month'] == months.index(month) + 1]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    print(f"Most Common Month: {df['month'].mode()[0]}")
    print(f"Most Common Day: {df['day_of_week'].mode()[0]}")
    print(f"Most Common Hour: {df['Start Time'].dt.hour.mode()[0]}")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    print(f"Common Start Station: {df['Start Station'].mode()[0]}")
    print(f"Common End Station: {df['End Station'].mode()[0]}")

    df['Route'] = df['Start Station'] + " to " + df['End Station']
    print(f"Common Route: {df['Route'].mode()[0]}")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    mean_travel = df['Trip Duration'].mean()

    print(f"Total Travel Time: {total_travel / 3600:.2f} hours")
    print(f"Average Travel Time: {mean_travel / 60:.2f} minutes")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...')
    start_time = time.time()

    print("User Types:\n", df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Counts:\n", df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print(f"\nEarliest Birth Year: {int(df['Birth Year'].min())}")
        print(f"Most Common Birth Year: {int(df['Birth Year'].mode()[0])}")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
