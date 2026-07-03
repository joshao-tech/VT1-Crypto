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
