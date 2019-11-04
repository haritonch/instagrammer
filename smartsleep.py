from time import sleep
from random import random

def smartsleep(base=1, scale=0.1):
    sleep(base + random()*scale)
