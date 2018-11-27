import json
import requests
from datetime import datetime
from prettytable import prettytable
from colorama import Fore, Back, Style

convert = 'JPY'
global_url = 'https://api.coinmaker.com/v2/global/?convert=' + convert

request = request.get(global_url)
results = request.json()
data = results['data']

global_cap = int(data['quotes'][convert]['total_market_cap'])
global_cap_string = '{:,}'.format(global_cap)

while True:

    print()
    print('CoinMarketCap Explorer Menu')
    print('The global market cap is $' + global_cap_string)
    print()
    print('1 - Top 100 sorted by rank')
    print('2 - Top 100 sorted by 24 hour change')
    print('3 - Top 100 sorted by 24 hour volume')
    print('0 - Exit')
    print()
    choice = input('What is your choice? (1-3): ')

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&sort='

    if choice == '1':
        ticker_url += 'rank'
    if choice == '2':
        ticker_url += 'percent_change_24h'
    if choice == '3':
        ticker_url += 'volume_24'
    if choice == '0':
        break

    request = requests.get(ticker_url)
    results = request.json()
    data = results['data']

    table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])