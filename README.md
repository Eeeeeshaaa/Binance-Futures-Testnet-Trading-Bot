# Binance-Futures-Testnet-Trading-Bot

Overview

A Python-based trading bot for Binance Futures Testnet (USDT-M) that supports Market, Limit, and Stop orders through a Command Line Interface (CLI).

The application provides:

Market Order Placement
Limit Order Placement
Stop Order Placement (Bonus)
BUY and SELL support
Input validation
Logging of requests, responses, and errors
Structured and reusable code architecture
Exception handling for API and network failures

Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── main.py
├── .env
├── requirements.txt
└── README.md

Requirements
Python 3.10+
Binance Demo/Testnet API Key
Internet Connection

Supported Order Types
1. Market Order - Executes immediately at the current market price.

2. Limit Order - Executes only when the specified price is reached.

3. Stop Order - Executes when the specified stop price is triggered.

Input Validation

The application validates:

Symbol format
Order side (BUY/SELL)
Order type
Quantity > 0
Price > 0 for Limit and Stop orders
Required arguments

Error Handling

The bot handles:

Invalid CLI arguments
Invalid order parameters
Binance API exceptions
Network failures
Missing API credentials

Assumptions
User has a valid Binance Demo/Testnet account.
User has sufficient virtual USDT balance.
Internet connectivity is available.
API keys are stored securely in .env.

Author
Eesha Kaul
