import random
def roll(auth, args):
    max_roll = 100
    if len(args) > 0:
        max_roll = int(args[0])
    return f'@{auth} rolls {str(random.randrange(0,max_roll))}'