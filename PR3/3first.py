import struct


def create_d_structures(data, address):
    result = []
    for d_address in struct.unpack('>4I', data[address:address + 16]):
        d1 = struct.unpack('>Q', data[d_address:d_address + 8])[0]
        d2 = list(struct.unpack('>3B', data[d_address + 8:d_address + 11]))

        result.append({
            'D1': d1,
            'D2': d2
        })

    return result


def f31(data):
    a2 = struct.unpack('>2s', data[26:28])[0].decode("utf-8")
    a3 = struct.unpack('>H', data[28:30])[0]
    a4 = struct.unpack('>H', data[30:32])[0]
    a5 = create_d_structures(data, 32)

    b1 = struct.unpack('>Q', data[4:12])[0]
    b2 = struct.unpack('>H', data[12:14])[0]
    b3 = struct.unpack('>I', data[14:18])[0]
    b4 = struct.unpack('>q', data[18:26])[0]

    c1 = struct.unpack('>H', data[b2:b2 + 2])[0]
    c2 = struct.unpack('>I', data[b2 + 2:b2 + 6])[0]
    c3 = struct.unpack('>2s', data[b2 + 6:b2 + 8])[0].decode("utf-8")
    c4 = struct.unpack('>B', data[b2 + 8:b2 + 9])[0]
    c5 = struct.unpack('>i', data[b2 + 9:b2 + 13])[0]

    out_dict = {
        'A1': {
            'B1': b1,
            'B2': {
                'C1': c1,
                'C2': c2,
                'C3': c3,
                'C4': c4,
                'C5': c5
            },
            'B3': b3,
            'B4': b4
        },
        'A2': a2,
        'A3': a3,
        'A4': a4,
        'A5': a5
    }

    return out_dict


print(f31((b'\xebTZN\xaaB\x19\x03\x0b\x07\xcd\'\x000JWT"\xa6\x128\xeb\xcc\x84\xedBbq'
           b'\xaf\x1c\xfd(\x00\x00\x00=\x00\x00\x00H\x00\x00\x00S\x00\x00\x00^U [\xef'
           b'\xdeYxi\xc2o~$\xdb\x16\x91}\xde\x08 \xaa\xa2e\xf1\xff:\xa0.\xe5H\xec\x18\xf2'
           b'\x850z\x1e_\xbc\xb10\x0f)\xa7\x8d(\xef\x1eMw\xd1\xa0;j\x1d\x9am<')))
