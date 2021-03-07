import hashlib
import random


def get_random_hash(len=64):
    return hashlib.sha256(str(random.getrandbits(len)).encode("utf-8")).hexdigest()
