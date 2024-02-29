from functools import lru_cache, wraps

import numpy as np


def np_cache(function):
    @lru_cache()
    def cached_wrapper(hashable_array):
        array = np.array(hashable_array)
        return function(array)

    @wraps(function)
    def wrapper(array):
        return cached_wrapper(tuple(array))

    # copy lru_cache attributes over too
    wrapper.cache_info = cached_wrapper.cache_info  # type: ignore
    wrapper.cache_clear = cached_wrapper.cache_clear  # type: ignore

    return wrapper
