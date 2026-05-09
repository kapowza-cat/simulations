import base64
import random

def encode(decode,base,skip=False):
    if isinstance(decode, bytes) and not skip:
        b = to_s(decode)
    else:
        b = decode
    if base == 16:
        return base64.b16encode(b.encode()).decode() if not skip else base64.b16encode(b)
    elif base == 32:
        return base64.b32encode(b.encode()).decode() if not skip else base64.b32encode(b)
    elif base == 64:
        return base64.b64encode(b.encode()).decode() if not skip else base64.b64encode(b)
    elif base == 85:
        return base64.b85encode(b.encode()).decode() if not skip else base64.b85encode(b)

def decode(decode,base,skip=False):
    if isinstance(decode, bytes) and not skip:
        b = to_s(decode)
    else:
        b = decode
    if base == 16:
        return base64.b16decode(b.encode()).decode() if not skip else base64.b16decode(b)
    elif base == 32:
        return base64.b32decode(b.encode()).decode() if not skip else base64.b32decode(b)
    elif base == 64:
        return base64.b64decode(b.encode()).decode() if not skip else base64.b64decode(b)
    elif base == 85:
        return base64.b85decode(b.encode()).decode() if not skip else base64.b85decode(b)
    
def to_b(d):
    return d.encode()

def to_s(d):
    return d.decode()

def xor_enc(d, k):
    if isinstance(d, str): d = d.encode()
    if isinstance(k, str): k = k.encode()
    return bytes([d[i] ^ k[i % len(k)] for i in range(len(d))])

def read_txt(n):
    d = {}
    with open(n, 'r') as f:
        for line in f:
            if ":" in line:
                k, v = line.strip().split(":")
                d[k] = [int(x) for x in v.split(",")]
    return d

def caesar(data, key):
    d = data.encode() if isinstance(data, str) else data
    return bytes([(b + key) % 256 for b in d])

def uncaesar(data, key):
    d = data.encode() if isinstance(data, str) else data
    return bytes([(b - key) % 256 for b in d])

def weave(data, key):
    d = data.encode() if isinstance(data, str) else data
    k = key.encode() if isinstance(key, str) else key
    
    result = bytearray()
    d_idx = 0
    interval = 3
    
    for i in range(len(k)):
        result.append(k[i])
        chunk = d[d_idx : d_idx + interval]
        result.extend(chunk)
        d_idx += interval
    
    if d_idx < len(d):
        result.extend(d[d_idx:])
        
    return bytes(result)

def unweave(woven_data, key_length):
    k_res = bytearray()
    d_res = bytearray()
    
    idx = 0
    interval = 3
    found_key_bytes = 0
    
    while idx < len(woven_data):
        if found_key_bytes < key_length:
            k_res.append(woven_data[idx])
            idx += 1
            found_key_bytes += 1
            
            chunk = woven_data[idx : idx + interval]
            d_res.extend(chunk)
            idx += interval
        else:
            d_res.extend(woven_data[idx:])
            break
            
    return bytes(d_res), bytes(k_res)

keys = read_txt("keys.txt")
indexable = list(keys.keys())
message = "b'+Zjq|_3t/c#G+7qj!!~)+bZ>*}?n+3bu~nd4/-ac/ri_@x2g+Kna+YfR%K}r!Uxb+uyv!a*7@ZxN~nnp*iH?~$Pg|m;d^Tfo*^+%@vwx~S1s*(pf!-s*-|aLd4jXJiGZw>uZa'"

#mode = input("Select a mode [e/d]")
mode = "d"

if mode == "e":
    key, code = random.choice(list(keys.items()))
    key = encode(key,85)
    print(key)
    #prevent bots from reading
    step = xor_enc(message,key)
    #prevent humans from reading
    for i in code:
        step = encode(step,i)
    #main encryption
    reverse_key = key[::-1]
    step = xor_enc(step,reverse_key)
    step = weave(step,reverse_key)
    caesarkey = random.randint(1,99)
    step = caesar(step,caesarkey)
    step = encode(step,85,True)
    step = weave(step,indexable[caesarkey])
elif mode == "d":
    step = message
    step = to_b(step)
    step, caesarkey = unweave(step,30)
print(step)
print(caesarkey)

