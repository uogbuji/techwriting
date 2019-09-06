import random
def file_num_writer(fp):
    runtotal = 0
    while True:
        num = yield
        runtotal += num
        print(num, runtotal, file=fp)

with open('/tmp/spam.txt', 'w') as fp:
    handler = file_num_writer(fp)
    next(handler) # Prime coroutine

    for f in range(5):
        num = random.randint(0, 10)
        handler.send(num)

