import collections
from os import NGROUPS_MAX
import sys
sys.path.append("..")
from common import *

data = aoci(lambda x:x)
# print(data)

conversion = { 
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

Packet = collections.namedtuple("Packet", ["version","type","value"])
OpPacket = collections.namedtuple("OperatorPacket", ["version","type","ltype","len","value"])

def parse_packet(bn,hex=True):
    if(hex): bn = reduce(lambda acc,v: acc + conversion[v], bn,"")
    consumed = 0
    version = int(bn[:3],base=2)
    consumed += 3
    type = int(bn[3:6],base=2)
    consumed += 3
    if type == 4:
        start = 6
        final = ""
        curr = bn[start:start+5]
        while curr[0] == "1":
            start += 5
            consumed += 5
            final += curr[1:]
            curr = bn[start:start+5]
        start += 5
        consumed += 5
        final += curr[1:]
        number = int(final,base=2)
        return (Packet(version,type,number),consumed)
    else:
        length_id = int(bn[6])
        consumed += 1
        if length_id:
            npacks = int(bn[7:18],base=2)
            consumed += 11
            subpacks = []
            start = 18
            for i in range(npacks):
                packet, ncon = parse_packet(bn[start:],hex=False)
                if packet == None:
                    break
                subpacks.append(packet)
                start += ncon
                consumed += ncon
            return (OpPacket(version,type,length_id,npacks,subpacks),consumed)
        else:
            packlen = int(bn[7:22],base=2)
            consumed += 15
            subpacks = []
            total = 0
            start = 22
            while packlen != total:
                packet, ncon = parse_packet(bn[start:],hex=False)
                subpacks.append(packet)
                total += ncon
                start += ncon
                consumed += ncon
            return (OpPacket(version,type,length_id,packlen,subpacks),consumed)

def sum_packet(pack):
    if isinstance(pack,Packet): return pack.version
    return pack.version + sum([sum_packet(sp) for sp in pack.value])

# print("testing")
# print(parse_packet("D2FE28"))
# print(parse_packet("38006F45291200"))
# print(parse_packet("EE00D40C823060"))
# print(sum_packet(parse_packet("8A004A801A8002F478")[0]))
# print(sum_packet(parse_packet("620080001611562C8802118E34")[0]))
# print(sum_packet(parse_packet("C0015000016115A2E0802F182340")[0]))
# print(sum_packet(parse_packet("A0016C880162017C3686B18A3D4780")[0]))

pack,consumed = parse_packet(data)
# pprint(pack)
print(sum_packet(pack))
