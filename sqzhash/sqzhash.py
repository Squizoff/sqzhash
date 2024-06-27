import random

class SqzHash:
    def __init__(self, seed=None):
        self.prime1 = 0x9E3779B97F4A7C15FFFFFFFFFFFFFFFF
        self.prime2 = 0xBF58476D1CE4E5B9FFFFFFFFFFFFFFFF
        self.prime3 = 0x94D049BB133111EBFFFFFFFFFFFFFFFF
        self.prime4 = 0xC6D1D6E005CB0A09FFFFFFFFFFFFFFFF
        self.salt = None
        self._reset()
        if seed is None:
            seed = random.randint(0, 2**32 - 1)
        random.seed(seed)

    def _reset(self):
        self.hash_value1 = self.prime1
        self.hash_value2 = self.prime2
        self.hash_value3 = self.prime3
        self.hash_value4 = self.prime4

    def set_salt(self, salt):
        self.salt = salt

    def update(self, input_data):
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')
        if self.salt:
            input_data = self.salt.encode('utf-8') + input_data

        for byte in input_data:
            self.hash_value1 = (self.hash_value1 + ((byte ^ self.prime1) << 8) - self.prime2) % (2 ** 64)
            self.hash_value2 = (self.hash_value2 + ((byte ^ self.prime2) << 16) - self.prime3) % (2 ** 64)
            self.hash_value3 = (self.hash_value3 + ((byte ^ self.prime3) << 24) - self.prime4) % (2 ** 64)
            self.hash_value4 = (self.hash_value4 + ((byte ^ self.prime4) << 32) - self.prime1) % (2 ** 64)
            for _ in range(0xC1):
                self._mix_hash_values()
            self._nonlinear_transform()

    def _mix_hash_values(self):
        self.hash_value1 ^= (self.hash_value2 >> 32) | (self.hash_value3 << 32)
        self.hash_value2 ^= (self.hash_value3 >> 32) | (self.hash_value4 << 32)
        self.hash_value3 ^= (self.hash_value4 >> 32) | (self.hash_value1 << 32)
        self.hash_value4 ^= (self.hash_value1 >> 32) | (self.hash_value2 << 32)
        self.hash_value1 = (self.hash_value1 + self.prime1) % (2 ** 64)
        self.hash_value2 = (self.hash_value2 + self.prime2) % (2 ** 64)
        self.hash_value3 = (self.hash_value3 + self.prime3) % (2 ** 64)
        self.hash_value4 = (self.hash_value4 + self.prime4) % (2 ** 64)

    def _nonlinear_transform(self):
        self.hash_value1 = ((self.hash_value1 ^ (self.hash_value2 << 32)) - (self.hash_value3 >> 32)) % (2 ** 64)
        self.hash_value2 = ((self.hash_value2 ^ (self.hash_value3 << 32)) - (self.hash_value4 >> 32)) % (2 ** 64)
        self.hash_value3 = ((self.hash_value3 ^ (self.hash_value4 << 32)) - (self.hash_value1 >> 32)) % (2 ** 64)
        self.hash_value4 = ((self.hash_value4 ^ (self.hash_value1 << 32)) - (self.hash_value2 >> 32)) % (2 ** 64)

    def _finalize(self):
        self.hash_value1 ^= (self.hash_value2 << 32) | (self.hash_value3 >> 32)
        self.hash_value2 ^= (self.hash_value3 << 32) | (self.hash_value4 >> 32)
        self.hash_value3 ^= (self.hash_value4 << 32) | (self.hash_value1 >> 32)
        self.hash_value4 ^= (self.hash_value1 << 32) | (self.hash_value2 >> 32)

    def hexdigest(self):
        self._finalize()
        combined_hash = (self.hash_value1 << 192) | (self.hash_value2 << 128) | (
                self.hash_value3 << 64) | self.hash_value4
        hex_hash = format(combined_hash, '064x')
        return hex_hash

    def digest(self):
        hex_hash = self.hexdigest()
        return bytes.fromhex(hex_hash)

    def reset(self):
        self._reset()

def hash_string(input_string):
    hasher = SqzHash()
    hasher.update(input_string)
    return hasher.hexdigest()

def hash_file(file_path):
    hasher = SqzHash()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()