print("BALANCE SCRIPT STARTED")
from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    testnet=True
)

balances = client.futures_account_balance()

for item in balances:
    if float(item["balance"]) > 0:
        print(item)