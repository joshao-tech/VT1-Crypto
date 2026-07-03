from binance.client import Client
from app.config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_SECRET_KEY
)

def get_usdt_symbols():
    exchange = client.futures_exchange_info()

    symbols = []

    for item in exchange["symbols"]:

        if item["quoteAsset"] != "USDT":
            continue

        if item["status"] != "TRADING":
            continue

        symbols.append(item["symbol"])

    return symbols


if __name__ == "__main__":

    usdt = get_usdt_symbols()

    print("USDT 永續數量：", len(usdt))

    print(usdt[:20])
 
