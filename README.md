# Python_Assignment1
This is Assignment1 for advanced programming in python course, this program can filter out top N cryptocurrencies by market capitalization 

## Installation
To launch this program, install pycoingecko is necessary

PyPI
```
pip install pycoingecko
```
or from source
```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```


## Usage
```
## launch the program on terminal ##
python3 main.py

```

## Examples
When you run the code:
```
## You will enter an integer ##
N = 2 

# Output#
{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 42133, 'market_cap': 796206779925, 'market_cap_rank': 1, 'fully_diluted_valuation': 888127748103, 'total_volume': 29515454712, 'high_24h': 43081, 'low_24h': 41877, 'price_change_24h': -550.171762894766, 'price_change_percentage_24h': -1.28895, 'market_cap_change_24h': -11996136655.509644, 'market_cap_change_percentage_24h': -1.4843, 'circulating_supply': 18826506.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -34.97437, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 62044.66803, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T05:40:27.549Z'}
{'id': 'ethereum', 'symbol': 'eth', 'name': 'Ethereum', 'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880', 'current_price': 2844.32, 'market_cap': 335454490728, 'market_cap_rank': 2, 'fully_diluted_valuation': None, 'total_volume': 22054475016, 'high_24h': 2968.55, 'low_24h': 2830.06, 'price_change_24h': -90.079350963789, 'price_change_percentage_24h': -3.06977, 'market_cap_change_24h': -10839246994.92688, 'market_cap_change_percentage_24h': -3.13007, 'circulating_supply': 117678225.499, 'total_supply': None, 'max_supply': None, 'ath': 4356.99, 'ath_change_percentage': -34.70496, 'ath_date': '2021-05-12T14:41:48.623Z', 'atl': 0.432979, 'atl_change_percentage': 656952.58672, 'atl_date': '2015-10-20T00:00:00.000Z', 'roi': {'times': 89.15146099636219, 'currency': 'btc', 'percentage': 8915.14609963622}, 'last_updated': '2021-09-26T05:40:45.044Z'}

```
