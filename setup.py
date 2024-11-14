import pandas as pd
import pymysql
import requests
from sqlalchemy import create_engine, text

# Define function to fetch intraday data
def fetch_intraday_data(ticker, interval='5min'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey=F3KK99CDFCPI5WM6'
    response = requests.get(url)
    data = response.json()
    
    time_series = data.get(f'Time Series ({interval})', {})
    if not time_series:
        print(f"No data returned for {ticker}")
        return None
    
    df = pd.DataFrame(time_series).T
    df.index.name = 'timestamp'
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df.reset_index(inplace=True)
    df = df.sort_index()
    df['ticker'] = ticker
    return df

# Test fetch_intraday_data to confirm data retrieval
test_data = fetch_intraday_data('IBM')
print("Sample fetched data:")
print(test_data.head())  # Check if data is retrieved correctly

# Database connection setup
db_config = {
    "host": "localhost",
    "user": "root",
    "passwd": "Spelpaloid23#",
    "database": "intraday_trading"
}

# Establish SQLAlchemy connection for pandas compatibility
engine = create_engine(f'mysql+pymysql://root:Spelpaloid23#@localhost/intraday_trading')

# Create table if it doesn't exist
with engine.connect() as connection:
    connection.execute(text('''
    CREATE TABLE IF NOT EXISTS intraday_prices (
        ticker VARCHAR(10),
        timestamp DATETIME,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume INT,
        PRIMARY KEY (ticker, timestamp)
    )
    '''))

# Function to get the latest timestamp for a ticker
def get_latest_timestamp(ticker):
    query = text("SELECT MAX(timestamp) FROM intraday_prices WHERE ticker = :ticker")
    with engine.connect() as connection:
        result = connection.execute(query, {"ticker": ticker}).fetchone()
    return result[0] if result else None

# Function to store data to the database
def store_data_to_db(data, latest_timestamp):
    if data is not None:
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        if latest_timestamp:
            if isinstance(latest_timestamp, str):
                latest_timestamp = pd.to_datetime(latest_timestamp)
            data = data[data['timestamp'] > latest_timestamp]
        
        if not data.empty:
            data.to_sql('intraday_prices', engine, if_exists='append', index=False)
            print(f"Inserted {len(data)} rows for {data['ticker'].iloc[0]}")
        else:
            print("No new data to store")
    else:
        print("No data to store")


# Main function to fetch and store data
def main():
    tickers = ["MSFT", "IBM"]
    for ticker in tickers:
        latest_timestamp = get_latest_timestamp(ticker)
        data = fetch_intraday_data(ticker)
        store_data_to_db(data, latest_timestamp)

if __name__ == "__main__":
    main()

# Query data from the database within a time range
def query_data(ticker, start_time, end_time):
    query = text("""
    SELECT * FROM intraday_prices
    WHERE ticker = :ticker AND timestamp BETWEEN :start_time AND :end_time
    ORDER BY timestamp DESC
    """)
    with engine.connect() as connection:
        df = pd.read_sql(query, connection, params={"ticker": ticker, "start_time": start_time, "end_time": end_time})
    return df

# Test query with a broader date range
print("\nQuerying data for IBM over a broader date range:")
df = query_data('IBM', '2024-01-01 00:00:00', '2024-12-31 23:59:59')
print(df)

# Check if data is available before plotting
if not df.empty:
    df.set_index('timestamp').close.plot()
else:
    print("No data available to plot for the specified range.")
