def zigzag(period):
    while True:
        yield from range(period)
        yield from range(period, 0, -1)

