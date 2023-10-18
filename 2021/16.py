ls = open('./input.txt', 'r').read().split('\n')[:-1][0]

""" Part 1 """

bits = ''
for value in ls:
    bits += str(bin(int(value, 16))[2:].zfill(4))

# packets with type ID == 4 are a literal value
# these have groups of 5 bits that start with 1 and if it starts with a 0 then its the last

# packet with type ID != 4 are operator packets, contains one or more packets
# if the 7th bit is 0, then the next 15 bits make a number that represents the total number of bits in the packet
# if its 1, then its the next 11 bits represents the number of subpackets.

packet_version_bits = ''
packet_type_id_bits = ''

length_type_id = -1

num_of_subpackets_bits = ''
num_of_bits_bits = ''

literal_value_bits = ''
last_literal_value_bits_num = 0
add_bits = False

for i in range(len(bits)):
    if len(packet_version_bits) != 3:
        packet_version_bits += bits[i:i+1]
    elif len(packet_type_id_bits) != 3:
        packet_type_id_bits += bits[i:i+1]
    else:
        packet_version = int(packet_version_bits, 2)
        packet_type_id = int(packet_type_id_bits, 2)
        if packet_type_id != 4:  # operator packet
            if length_type_id == -1:
                length_type_id = int(bits[i:i+1])
            else:
                if length_type_id == 1:  # next 11 bits will show the amount of subpackets
                    if len(num_of_subpackets_bits) != 11:
                        num_of_subpackets_bits += bits[i:i+1]
                    elif len(num_of_subpackets_bits) == 11:
                        num_of_subpackets = int(num_of_subpackets_bits, 2)
                        # new packet
                elif length_type_id == 0:  # next 15 bits will show the amount of bits 
                    if len(num_of_bits_bits) != 15:
                        num_of_bits_bits += bits[i:i+1]
                    elif len(num_of_bits_bits) == 15:
                        num_of_bits = int(num_of_bits_bits, 2)
                        # new packet
        elif packet_type_id == 4:  # literal value packet
            if add_bits or last_literal_value_bits_num != 0:
                literal_value_bits += bits[i:i+1]
            if len(literal_value_bits) % 4 == 0 and add_bits:  # this will stop adding to the string
                add_bits = False
            elif not add_bits and last_literal_value_bits_num == 0:
                if bits[i:i+1] == '0':
                    last_literal_value_bits_num = len(literal_value_bits)
                else:
                    add_bits = True
            elif len(literal_value_bits) % 4 == 0:
                pass
                # new packet  

""" Part 2 """

