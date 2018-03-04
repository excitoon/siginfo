def from_bytes(bytes):
    return int.from_bytes(bytes, byteorder='little')

def from_be_bytes(bytes):
    return int.from_bytes(bytes, byteorder='big')

def read_block(bytes, offset, size):
    assert len(bytes) >= offset + size
    return bytes[offset:offset+size]

def read_block_until_end(bytes, offset):
    assert len(bytes) >= offset
    return bytes[offset:]

def read_byte(bytes, offset):
    return from_bytes(read_block(bytes, offset, 1))

def read_word(bytes, offset):
    return from_bytes(read_block(bytes, offset, 2))

def read_be_word(bytes, offset):
    return from_be_bytes(read_block(bytes, offset, 2))

def read_dword(bytes, offset):
    return from_bytes(read_block(bytes, offset, 4))

class Pipe(object):
    def __init__(self, bytes):
        self.bytes = bytes
        self.offset = 0

    def read_block(self, size):
        result = read_block(self.bytes, self.offset, size)
        self.offset += size
        return result

    def read_block_until_end(self):
        result = read_block_until_end(self.bytes, self.offset)
        self.offset += len(result)
        return result

    def read_byte(self):
        result = read_byte(self.bytes, self.offset)
        self.offset += 1
        return result

    def read_word(self):
        result = read_word(self.bytes, self.offset)
        self.offset += 2
        return result

    def read_be_word(self):
        result = read_be_word(self.bytes, self.offset)
        self.offset += 2
        return result

    def read_dword(self):
        result = read_dword(self.bytes, self.offset)
        self.offset += 4
        return result

    def read_packed_be_word(self):
        first = self.read_byte()
        if first & 0x80 != 0x80:
            return first
        else:
            return (first & 0x7f) << 8 | self.read_byte()

    def read_packed_be_dword(self):
        first = self.read_byte()
        if first & 0x80 != 0x80:
            return first
        elif first & 0xc0 != 0xc0:
            return (first & 0x7f) << 8 | self.read_byte()
        elif first & 0xe0 != 0xe0:
            first = (first & 0x3f) << 8 | self.read_byte()
        else:
            first = self.read_be_word()
        second = self.read_be_word()
        return first << 16 | second
