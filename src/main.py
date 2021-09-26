from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

coinList = cg.get_coins_markets("usd")

N = int(input("N = "))
i = 0
while i < N:
    print(coinList[i])
    i += 1
