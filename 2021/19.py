import time
import numpy as np
from collections import Counter

start_time = time.time()
ls = open('./input.txt').read().split('\n\n')
ls[-1] = ls[-1][:-1]

""" Part 1 390"""

rotations = [
    lambda cr: (cr[0], cr[1], cr[2]),
    lambda cr: (cr[2], cr[0], cr[1]),
    lambda cr: (cr[1], cr[2], cr[0]),
    lambda cr: (cr[0], cr[2], cr[1]),
    lambda cr: (cr[2], cr[1], cr[0]),
    lambda cr: (cr[1], cr[0], cr[2]),
]
orientations = [
    lambda cr: (cr[0], cr[1], cr[2]),
    lambda cr: (cr[0], cr[1], -cr[2]),
    lambda cr: (cr[0], -cr[1], cr[2]),
    lambda cr: (cr[0], -cr[1], -cr[2]),
    lambda cr: (-cr[0], -cr[1], -cr[2]),
    lambda cr: (-cr[0], cr[1], cr[2]),
    lambda cr: (-cr[0], -cr[1], cr[2]),
    lambda cr: (-cr[0], cr[1], -cr[2]),
]


class Beacon:
    def __init__(self, b_coord):
        self.distances = set()
        self.distance_key = {}
        self.coord = b_coord


def parse_scanner(scanner_text):
    beacons = []
    coords = scanner_text.split('\n')[1:]
    for beacon in coords:
        coord = [int(a) for a in beacon.split(',')]
        coord = (coord[0], coord[1], coord[2])
        beacons.append(Beacon(coord))
    return beacons


def update_distances(beacons_list1, beacons_list2=None, keep_old=False):
    for beacon in beacons_list1:
        if not keep_old:
            beacon.distances = set()
            beacon.distance_key = {}
        # for beacon_2 in beacons_list2:
        for beacon_2 in beacons_list1:
            if beacon != beacon_2:
                c = beacon.coord
                c2 = beacon_2.coord
                dis = ((c2[0] - c[0]) ** 2 + (c2[1] - c[1]) ** 2 + (c2[2] - c[2]) ** 2) ** 2
                if dis <= 6000000 ** 2:
                    beacon.distances.add(dis)
                    beacon.distance_key[dis] = c2


def part_1(ll):
    s0 = []
    scanners = []
    for scanner in ll:
        s_num = int(scanner[:15].split(' ')[2])
        if s_num == 0:
            s0 = parse_scanner(scanner)
        else:
            scanners.append(parse_scanner(scanner))
    # update_distances(s0, s0, False)
    update_distances(s0)
    for beacon_list in scanners:
        # update_distances(beacon_list, beacon_list, False)
        update_distances(beacon_list)
    current_i = 0
    while len(scanners) != 0:
        for bc in s0:
            for bc2 in scanners[current_i]:
                count = bc.distances.intersection(bc2.distances)
                if len(count) >= 11:
                    start_beacons = [bc, bc2]
                    break
            else:
                continue
            break
        else:
            current_i += 1
            continue
        # We did find 11 matching distances, so we need to:
        connected_coords = [[start_beacons[0].coord, start_beacons[1].coord]]
        for dis in count:
            connected_coords.append([start_beacons[0].distance_key[dis], start_beacons[1].distance_key[dis]])
        # - Find the offset and rotation
        pd = []
        for cc in connected_coords:
            for p in range(48):
                new = rotations[p // 8](orientations[p % 8]((cc[1][0], cc[1][1], cc[1][2])))
                pd.append((cc[0][0] - new[0], cc[0][1] - new[1], cc[0][2] - new[2]))
        ctr = Counter(pd)
        offset = ctr.most_common()[0][0]
        delta_index = list(ctr.keys()).index(offset)
        # - Apply this offset and rotation to the non s0 scanner
        for beacon in scanners[current_i]:
            coord = rotations[delta_index // 8](orientations[delta_index % 8](beacon.coord))
            beacon.coord = (coord[0] + offset[0], coord[1] + offset[1], coord[2] + offset[2])
        # - Add all of those converted coordinates to s0
        s0_coords = [bc.coord for bc in s0]
        beacons_to_add = []
        for beacon in scanners[current_i]:
            if beacon.coord not in s0_coords:
                beacons_to_add.append(beacon)
        # - Recalculate the distances
        # update_distances(beacons_to_add, s0, False)
        # update_distances(s0, beacons_to_add, False)
        s0 += beacons_to_add
        update_distances(s0)
        # - Delete that scanner from the scanner list
        scanners.pop(current_i)
        # - Set `current_i` back to 0
        current_i = 0
    print(len(s0))


part_1(ls)
print(f'Took {round(time.time() - start_time, 3)} seconds')

""" Part 2 13327"""
