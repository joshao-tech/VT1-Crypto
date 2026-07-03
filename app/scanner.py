import requests

BASE = "https://fapi.binance.com"

def get_usdt_symbols():
    url = BASE + "/fapi/v1/exchangeInfo"
    data = requests.get(url).json()

    symbols = []

    for s in data["symbols"]:
        if (
            s["quoteAsset"] == "USDT"
            and s["contractType"] == "PERPETUAL"
            and s["status"] == "TRADING"
        ):
            symbols.append(s["symbol"])

    return sorted(symbols)


if __name__ == "__main__":
    coins = get_usdt_symbols()
    print(len(coins))
    print(coins[:20])
import requests
import pandas as pd

BASE = "https://fapi.binance.com"

def get_klines(symbol, interval="4h", limit=500):
    url = BASE + "/fapi/v1/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
    }

    data = requests.get(url, params=params).json()

    df = pd.DataFrame(data)

    df = df.iloc[:, :6]
    df.columns = [
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    df = df.astype({
        "open": float,
        "high": float,
        "low": float,
        "close": float,
        "volume": float,
    })

    return df
