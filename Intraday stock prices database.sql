-- setup.sql

-- Create database
CREATE DATABASE IF NOT EXISTS intraday_trading;
USE intraday_trading;

-- Create table for storing intraday stock prices
CREATE TABLE IF NOT EXISTS intraday_prices (
    ticker VARCHAR(10) NOT NULL,
    timestamp DATETIME NOT NULL,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INT,
    PRIMARY KEY (ticker, timestamp)
);
