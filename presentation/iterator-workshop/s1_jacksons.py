import random


class random_jacksonserator:
    _triples = (
        ('A', 'B', 'C'),
        (1, 2, 3),
        ('Do', 'Re', 'Mi')
    )

    def __init__(self):
        self._curr_triple = random.choice(random_jacksonserator._triples)
        self._ix = 0

    def __next__(self):
        if self._ix >= len(self._curr_triple):
            raise StopIteration
        word = self._curr_triple[self._ix]
        self._ix += 1
        return word

    def __iter__(self):
        return self
