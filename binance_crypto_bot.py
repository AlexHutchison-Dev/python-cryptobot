from binance import Client
import secrets
import pandas as pd

client = Client(secrets.API_KEY, secrets.SECRET, testnet=True)


def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback))
    frame = frame.iloc[:, :6]
    frame.columns = ["Time", "Open", "High", "Low", "Close", "Volume"]
    frame = frame.set_index("Time")
    frame.index = pd.to_datetime(frame.index, unit="ms")
    frame = frame.astype(float)
    return frame


results = getminutedata("BTCUSDT", "1m", "30m")

print(results)

# for kline in client.get_historical_klines_generator(
#     "BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"
# ):
#     print(kline)
#     # do something with the kline
