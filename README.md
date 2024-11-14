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

```bash
pip install pandas pymysql SQLAlchemy requests matplotlib
