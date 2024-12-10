from helpers import *
from collections import *

ls = [list(a.strip()) for a in open('./input.txt').read().strip().split('\n')]
lsl = len(ls)

""" Part 1 """

antennas = defaultdict(list)
antinodes = set()

for ant in {c for row in ls for c in row if c != '.'}:
    antennas[ant] += find_val(ls, lambda x: x == ant)

for a in antennas:
    for i, (x1, y1) in enumerate(antennas[a]):
        for x2, y2 in antennas[a][i+1:]:
            nx1, ny1 = x1 + (x1 - x2), y1 + (y1 - y2)
            nx2, ny2 = x2 - (x1 - x2), y2 - (y1 - y2)
            if in_bounds(nx1, ny1, lsl):
                antinodes.add((nx1, ny1))
            if in_bounds(nx2, ny2, lsl):
                antinodes.add((nx2, ny2))

print(len(antinodes))

""" Part 2 """

antinodes = set()

for a in antennas:
    for i, (x1, y1) in enumerate(antennas[a]):
        for x2, y2 in antennas[a][i+1:]:
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))

            nx1, ny1 = x1 + (x1 - x2), y1 + (y1 - y2)
            nx2, ny2 = x2 - (x1 - x2), y2 - (y1 - y2)

            while in_bounds(nx1, ny1, lsl):
                antinodes.add((nx1, ny1))
                nx1, ny1 = nx1 + (x1 - x2), ny1 + (y1 - y2)
            while in_bounds(nx2, ny2, lsl):
                antinodes.add((nx2, ny2))
                nx2, ny2 = nx2 - (x1 - x2), ny2 - (y1 - y2)

print(len(antinodes))
