import json
import requests

ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array"

limit = 100
start = 1
sort = 'id'
convert = "USD"

choice = input("Do you want to enter any custom parameters? (y/n): ")

if choice == 'y':
    limit = input('What is the custom limit?: ')
    start = input('What is the customer start number?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is the local currenct?: ')

    ticker_url += '&limit' + limit + '&start' + start + '&sort' + sort + '&convert' + convert

    request = requests.get(ticker_url)
    results = request.json()

    print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

print()
for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])

        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hourly_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume)
        marketcap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(circulating_supply)
        price_string = '{:,}'.format(price)

        print(str(rank) + ': ' + name + '( '+ symbol + ')')
        print('Market cap: $' + marketcap_string)
        print('Price: $' + price_string)
        print('24 Volume: $' + volume_string)
        print('Hourly Change: $' + str(hourly_change) + '%')
        print('Week Change: $' +str(week_change) + '%')
        print('Total Supply: $' + total_supply_string)
        print('Circulating Supply: $' + circulating_supply_string)
        print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
        print()

        choice = input('Again? ')

        if choice == 'n':
            break 
