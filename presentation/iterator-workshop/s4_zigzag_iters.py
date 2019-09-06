def zigzag_iters(period):
    while True:
        yield range(period)
        yield range(period, 0, -1)
