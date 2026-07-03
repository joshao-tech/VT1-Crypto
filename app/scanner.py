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

        if item["contractType"] != "PERPETUAL":
            continue

        if item["status"] != "TRADING":
            continue

        symbols.append(item["symbol"])

    return sorted(symbols)


if __name__ == "__main__":

    data = get_usdt_symbols()

    print(f"共有 {len(data)} 個USDT永續")

    print(data[:20])
