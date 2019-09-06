class textfinder:
    def __init__(self, fulltext, delim='.'):
        self._fulltext = fulltext
        self._delim = delim
        self._ix = 0

    def __next__(self):
        if self._ix >= self._fulltext:
            raise StopIteration
        found = False
        while not found:
            if self._delim in self._fulltext[self._ix:]:
                ns = self._fulltext[self._ix:].split(self._delim, 1)[0]
            else:
                ns = self._fulltext[self._ix:]
            self._ix += len(ns)



