import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
        return cache_storage[key]
    return wrapper
