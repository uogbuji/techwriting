from random import random
def n_head_monty(win_count):
    head_count = 0
    while True:
        head = random() < 0.5 # Fastest coinflip in Py :)
        if head:
            yield 'H'
            head_count += 1
        else:
            yield 'T'
            head_count = 0
        if head_count == win_count: break

