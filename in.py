import os
import sys
import requests

day = sys.argv[1]
try:
    year = sys.argv[2]
except IndexError:
    year = 2024

inp = ''
if os.path.isfile(f'puzzle-inputs/{year}-{day}.txt'):
    inp = open(f'puzzle-inputs/{year}-{day}.txt').read().replace('\r', '')
else:
    link = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {
        'user-agent': 'https://github.com/aiden-perkins/advent-of-code',
        'cookie': f'session={open(".session").read()}'
    }
    inp = requests.get(link, headers=headers).content.decode().replace('\r', '')
    cache_txt = open(f'puzzle-inputs/{year}-{day}.txt', 'w')
    cache_txt.write(inp.replace('\r', ''))
    cache_txt.close()

txt = open('input.txt', 'w')
txt.write(inp.replace('\r', ''))
txt.close()

print(inp)
