from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cities_queue = deque(cities)
    cache = []
    time = 0

    while cities_queue:
        city = cities_queue.popleft().lower()
        if city in cache:
            idx = cache.index(city)
            if idx != len(cache) - 1:
                cache = cache[:idx] + cache[idx+1:] + [city]
            time += 1
            continue

        time += 5
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            cache = cache[1:]
            cache.append(city)
    
    return time