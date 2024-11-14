# Intraday Stock Price Tracker

This project is a Python-based application that fetches intraday stock price data from the Alpha Vantage API, stores it in a MySQL database, and enables data querying and visualization. The program is designed to support intraday trading analysis by automatically updating and storing new price data over specified intervals.

## Features

- **Fetch Intraday Stock Data**: Retrieves intraday price data from the Alpha Vantage API.
- **MySQL Storage**: Stores stock data in a MySQL database for persistent storage and analysis.
- **Data Querying**: Allows querying stored data by ticker and timestamp.
- **Data Visualization**: Supports plotting stock price trends over specified periods.

## Prerequisites

- **Python 3.6+**
- **MySQL Server**
- **MySQL Workbench** (optional, for database management)
- **API Key** from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) (free)

### Python Packages

Install the required packages via pip:

## How to Run SQL Queries in MySQL Workbench


Open MySQL Workbench and Connect to the Database:

Launch MySQL Workbench and log in to your MySQL server using your credentials.

In the Navigator panel on the left, locate and expand Schemas to see a list of available databases on your server.

Find the database named intraday_trading (created by your Python script) and click to expand it. You should see a Tables section with the table intraday_prices listed.

Open a New SQL Query Tab:

In the top menu, click on the + icon next to the existing tabs to open a new SQL query tab. This will provide you with a blank editor where you can write and execute SQL queries.

Run SQL Commands to View and Manage Data:

Use the SQL commands below to explore and manage the data stored in the intraday_prices table:

View all data: 
SELECT * FROM intraday_trading.intraday_prices;

Filter data by ticker symbol: 
SELECT * FROM intraday_trading.intraday_prices WHERE ticker = 'IBM';

FIlter data by data range: 
SELECT * FROM intraday_trading.intraday_prices
WHERE ticker = 'IBM' 
AND timestamp BETWEEN '2024-09-27 00:00:00' AND '2024-09-27 23:59:59';

View latest entries:
SELECT * FROM intraday_trading.intraday_prices 
ORDER BY timestamp DESC 
LIMIT 10;

Update Data:
UPDATE intraday_trading.intraday_prices
SET close = 150.50
WHERE ticker = 'IBM' AND timestamp = '2024-09-27 15:30:00';

Delete Data:
DELETE FROM intraday_trading.intraday_prices
WHERE ticker = 'IBM' AND DATE(timestamp) = '2024-09-27';


Execute Queries:

To run any of these queries, simply type or paste them into the SQL editor tab in MySQL Workbench and click the Execute (lightning bolt) button in the toolbar, or press Ctrl + Enter.
The results will appear in the output grid at the bottom of the Workbench window, showing the data you queried or confirming successful updates/deletions.


