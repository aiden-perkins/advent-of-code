import operator
import functools

ls = open('./input.txt', 'r').read().split('\n')[:-1][0]

""" Part 1 """

bits = ''
for b in ls:
    bits += str(bin(int(b, 16))[2:].zfill(4))

operations = {
    0: lambda x: sum([y[2] for y in x]),
    1: lambda x: functools.reduce(operator.mul, [y[2] for y in x]),
    2: lambda x: min([y[2] for y in x]),
    3: lambda x: max([y[2] for y in x]),
    5: lambda x: 1 if x[0][2] > x[1][2] else 0,
    6: lambda x: 1 if x[0][2] < x[1][2] else 0,
    7: lambda x: 1 if x[0][2] == x[1][2] else 0
}


def parse_multiple_packets(bit_string, packets_c):
    packets = []
    while bit_string != '':
        c_i = 6
        pv, ptid = int(bit_string[0:3], 2), int(bit_string[3:6], 2)
        if ptid != 4:
            c_i += 1
            ltid = int(bit_string[6:7], 2)
            if ltid == 0:
                c_i += 15
                packets_count = 0
                new_bits = bit_string[22:22 + int(bit_string[7:22], 2)]
            else:
                c_i += 11
                packets_count = int(bit_string[7:18], 2)
                new_bits = bit_string[18:]
            new_packets = parse_multiple_packets(new_bits, packets_count)
            for n_p in new_packets:
                c_i += n_p[3]
                pv += n_p[0]
            packets += [[pv, ptid, operations[ptid](new_packets), c_i]]
        else:
            n_b_s = ''
            for bit_group in range(len(bit_string[6:]) // 5):
                n_b_s += bit_string[7 + (bit_group * 5):((bit_group + 1) * 5) + 6]
                if bit_string[6 + (bit_group * 5):7 + (bit_group * 5)] == '0':
                    break
            c_i += (len(n_b_s) // 4) * 5
            lv = int(n_b_s, 2)
            packets.append([pv, ptid, lv, ((len(n_b_s) // 4) * 5) + 6])
        bit_string = bit_string[c_i:]
        if '1' not in bit_string or (len(packets) > 0 and len(packets) == packets_c):
            break
    return packets


total_version_nums = 0
ps = parse_multiple_packets(bits, 0)
for packet in ps:
    total_version_nums += packet[0]
print(ps[0][0])

""" Part 2 """

print(ps[0][2])
