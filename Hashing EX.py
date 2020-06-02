hash_table = [[] for _ in range(10)]

def hashing_func(key):
    return key % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)

def hashing_func(key):
    return key % len(hash_table)

def add(hash_table, key, value):
    hash_key = hashing_func(key)
    return hash_table[hash_key].append(value)

def remove(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print('Key {} deleted'.format(key))
    else:
        print('Key {} not found'.format(key))

def contains(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v
