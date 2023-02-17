import os

cache = dict()

def accessEnv(key: str, default = None) -> str:

    cached_value = cache.get(key)

    if cached_value is not None:
        return cached_value

    value = os.getenv(key)

    if value is None:
        return default
    
    cache[key] = value
    return value
