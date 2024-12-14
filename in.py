import os
import requests

line = input('[Day] (year): \n').split(' ')
day = line[0]
try:
    year = int(line[1])
except IndexError:
    year = 2024

inp = ''
if os.path.isfile(f'puzzle-inputs/{year}-{day}.txt'):
    inp = open(f'puzzle-inputs/{year}-{day}.txt').read()
else:
    link = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {
        'user-agent': 'https://github.com/aiden-perkins/advent-of-code',
        'cookie': f'session={open(".session").read()}'
    }
    inp = requests.get(link, headers=headers).content.decode()
    cache_txt = open(f'puzzle-inputs/{year}-{day}.txt', 'w')
    cache_txt.write(inp)
    cache_txt.close()

txt = open('input.txt', 'w')
txt.write(inp)
txt.close()

print(inp)
