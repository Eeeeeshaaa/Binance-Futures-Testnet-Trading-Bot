import os

from dotenv import load_dotenv
from binance.client import Client
load_dotenv()
class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        print("API KEY= ", api_key[:10] if api_key else None)
        print("SECRET EXISTS=",bool(api_secret))

        if not api_key or not api_secret:
            raise ValueError(
                "API credentials not found in .env"
            )

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )
