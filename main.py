import sys
import binascii
def disasm(op):
    op = int.from_bytes(op, byteorder="big") 
    opstart = op >> 12
    if opstart == 0x6:
        return ("LD", hex(op & 0x0F00), hex(op & 0x00FF))
    elif opstart == 0xA:
        return ("LD", "i", hex(op & 0x0FFF))
    elif opstart == 0xD:
        return ("DRW", hex(op & 0x0F00), hex(op & 0x00F0), hex(op & 0xF)) 
f = open(sys.argv[1], "rb")
while True:
    x = f.read(2)
    if x != b"":
        print(binascii.hexlify(x), disasm(x))
    else: break
