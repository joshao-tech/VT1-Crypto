import os

# OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Binance API
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY", "")

# Scanner Settings
TIMEFRAME = "4h"
EMA_FAST = 20
EMA_SLOW = 60
RSI_PERIOD = 14
ADX_PERIOD = 14
