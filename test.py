from operator import truediv
from re import T
import sys
import time
import random

def textreader():
  for letter in prompt:
    print(letter, end="")
    time.sleep(0.05)

class Slime:
  hp = random.randint(3,7)
  atk = 1

class Dog:
  hp = random.randint(6,9)
  atk = 2

class Dragon:
  hp = random.randint(15,20)
  atk = 4

enemy = (Slime, Dog, Dragon)

print(random.choice(enemy))