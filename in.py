import requests
import sys

day = int(sys.argv[1])
try:
    year = int(sys.argv[2])
except IndexError:
    year = 2021
link = f'https://adventofcode.com/{year}/day/{day}/input'
cookies = {'session': ''}
inp = requests.get(link, cookies=cookies).content.decode('utf-8')
txt = open('input.txt', 'w')
txt.write(inp)
txt.close()
print(inp)
