import requests
import sys

line = input('[Day] (year): \n').split(' ')
day = line[0]
try:
    year = int(line[1])
except IndexError:
    year = 2023
link = f'https://adventofcode.com/{year}/day/{day}/input'
cookies = {'session': ''}
inp = requests.get(link, cookies=cookies).content.decode('utf-8')
txt = open('input.txt', 'w')
txt.write(inp)
txt.close()
print(inp)
