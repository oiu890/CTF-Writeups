import ctypes, ctypes.util

# load glibc rand/srand so results match the binary exactly
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.srand.argtypes = [ctypes.c_uint]
libc.rand.restype = ctypes.c_int

# hardcoded encrypted bytes from decrypt()
arr = bytes([
    0x14,0xbe,0x2f,0x89,0xf2,0xc5,0xfa,0x1c,0x43,0xdc,
    0x6b,0x9e,0x33,0xda,0xfe,0x87,0xf1,0x49,0x70,0xd9,
    0x28,0x80,0x09,0x8f,0xb5,0x8d,0xc2,0x5e,0x1b,0xd6,
    0x1c,0xc0,0x01,0x8a,0xbe,0xc3,0x9d
])

def gen_key_half(seed, count=5):
    """Generate count key bytes from glibc rand() using the C expression:
       (char)rand() + (char)(rand()/0xff), then assigned to char."""
    libc.srand(seed)
    out = []
    for _ in range(count):
        r = libc.rand()
        a = r & 0xff
        if a >= 0x80:  # interpret as signed char
            a -= 0x100
        b = (r // 0xff) & 0xff
        if b >= 0x80:
            b -= 0x100
        out.append((a + b) & 0xff)  # assignment to unsigned 8-bit
    return out

def gen_key(seed1, seed2):
    return gen_key_half(seed1) + gen_key_half(seed2)

def decrypt_with(key):
    return bytes(c ^ key[i % 10] for i, c in enumerate(arr))

best = None
for s1 in range(1, 39):   # gappleX range
    for s2 in range(1, 19):  # gappleY range
        key = gen_key(s1, s2)
        dec = decrypt_with(key)
        score = sum(32 <= b < 127 for b in dec) / len(dec)
        if best is None or score > best[0]:
            best = (score, s1, s2, key, dec)

score, seed1, seed2, key, dec = best
print(f"Best candidate score={score:.3f} seeds=({seed1},{seed2}) key={[hex(x) for x in key]}")
print("Decrypted bytes:", dec)
print("Flag:", dec.rstrip(b'\x00').decode('ascii', errors='replace'))
