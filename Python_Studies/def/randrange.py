import random
from random import randrange

def throw_dice():
    throw_dice_1 = randrange(1,7)
    throw_dice_2 = randrange(1,7)
    result = throw_dice_1 + throw_dice_2
    return result

print(throw_dice())


