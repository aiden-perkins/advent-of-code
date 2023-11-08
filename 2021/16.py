ls = open('./input.txt', 'r').read().split('\n')[:-1][0]

""" Part 1 """

ls = 'C200B40A82'
bits = ''
for b in ls:
    bits += str(bin(int(b, 16))[2:].zfill(4))


def parse_multiple_packets(bit_string):
    packets = []
    while bit_string != '':
        c_i = 6
        pv, ptid = int(bit_string[0:3], 2), int(bit_string[3:6], 2)
        if ptid != 4:
            c_i += 1
            ltid = int(bit_string[6:7], 2)
            if ltid == 0:
                c_i += 15
                new_bits = bit_string[22:22 + int(bit_string[7:22], 2)]
            else:
                c_i += 11
                new_bits = bit_string[18:]
            packets += [[pv, ptid, 'sub', c_i]]
            new_packets = parse_multiple_packets(new_bits)
            for n_p in new_packets:
                c_i += n_p[3]
            packets += new_packets
        else:
            n_b_s = ''
            for bit_group in range(len(bit_string[6:]) // 5):
                n_b_s += bit_string[6 + (bit_group * 5):((bit_group + 1) * 5) + 6]
                if bit_string[6 + (bit_group * 5):7 + (bit_group * 5)] == '0':
                    break
            c_i += len(n_b_s)
            packets.append([pv, ptid, int(n_b_s, 2), len(n_b_s) + 6])
        bit_string = bit_string[c_i:]
        if '1' not in bit_string:
            break
    return packets


total_version_nums = 0
ps = parse_multiple_packets(bits)
for packet in ps:
    total_version_nums += packet[0]
print(total_version_nums)

""" Part 2 """

print(ps)
