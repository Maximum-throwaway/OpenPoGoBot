# -*- coding: utf-8 -*-

import time
from math import ceil
from random import random, randint


def sleep(seconds, delta=0.3):
    jitter = ceil(delta * seconds)
    sleep_time = randint(int(seconds - jitter), int(seconds + jitter))
    time.sleep(sleep_time)


def random_lat_long_delta():
    # Return random value from [-.000025, .000025]. Since 364,000 feet is equivalent to one degree of latitude, this
    # should be 364,000 * .000025 = 9.1. So it returns between [-9.1, 9.1]
    return ((random() * 0.00001) - 0.000005) * 5

def random_throw_accuracy(randomize):
    # This is a function that can optionally randomize the accuracy of your throws. Nobody should be chucking 100
    # perfect throws in a row. This implementation seems to range from a "nice" to "perfect". Setting it below 1
    # in my tests just causes it to fail, so I'm not sure what a perfectly normal throw value would be.
    if randomize:
        return random.uniform(1.000,1.950)
    else:
        return 1.950