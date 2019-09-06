def zigzag(period):
    while True:
        for n in range(period):
            yield n
        for n in range(period, 0, -1):
            yield n
