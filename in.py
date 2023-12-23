import requests

line = input('[Day] (year): \n').split(' ')
day = line[0]
try:
    year = int(line[1])
except IndexError:
    year = 2023
link = f'https://adventofcode.com/{year}/day/{day}/input'
headers = {
    'user-agent': 'https://github.com/aiden-perkins/advent-of-code',
    'cookie': 'session='
}
inp = requests.get(link, headers=headers).content.decode()
txt = open('input.txt', 'w')
txt.write(inp)
txt.close()
print(inp)
