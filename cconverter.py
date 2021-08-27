import requests
cache = {}
i = input().lower()
user = requests.get(f'http://www.floatrates.com/daily/{i}.json')
if i == 'usd':
    cache['eur'] = user.json()['eur']['rate']
elif i == 'eur':
    cache['usd'] = user.json()['usd']['rate']
else:
    cache['eur'] = user.json()['eur']['rate']
    cache['usd'] = user.json()['usd']['rate']
while True:
    ex = input()
    if not ex:
        break
    else:
        cash = int(input())
        print('Checking the cache...')
        if ex in cache:
            print('Oh! It is in the cache!')
            print(f'You received {(user.json()[ex]["rate"]) * cash} {ex.upper()}.')
        else:
            cache[ex] = user.json()[ex]['rate']
            print('Sorry, but it is not in the cache!')
            print(f'You received {(user.json()[ex]["rate"]) * cash} {ex.upper()}.')
