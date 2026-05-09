import random

# The symbols we'll use for the keys
syms = "+-/*%!@^|~"
# The bases corresponding to those symbols (you can expand this)
bases = [32, 64, 85]

def gen_vault(n=100):
    vault = {}
    while len(vault) < n:
        # Generate a random 25-character string
        k = ''.join(random.choice(syms) for _ in range(30))
        # Generate a random sequence of encoding steps of any length (e.g., 5 steps)
        v = [random.choice(bases) for _ in range(5)]
        vault[k] = v
    return vault

# Create the dictionary
data_map = gen_vault()

def write_txt(n, d):
    with open(n, 'w') as f:
        for k, v in d.items():
            # Join list of ints into a comma-separated string
            val_str = ",".join(map(str, v))
            f.write(f"{k}:{val_str}\n")

# Example: Print the first key and its encoding path
first_key = list(data_map.keys())[0]
print(f"Key: {first_key}")
print(f"Path: {data_map[first_key]}")
write_txt("keys.txt",data_map)