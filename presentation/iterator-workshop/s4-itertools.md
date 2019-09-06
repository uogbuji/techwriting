
```
import itertools
it = itertools.chain(range(5), range(5, 0, ‑1), range(5))
list(it)

list_of_iters = [range(5), range(5, 0, ‑1), range(5)]
it = itertools.chain(*list_of_iters)
list(it)
```

```
import itertools
def forth_back_forth(n):
    yield range(n)
    yield range(n, 0, -1)
    yield range(n)
it = itertools.chain(*forth_back_forth(3))
list(it)
```

```
it = zigzag_iters(2)
next(it)
```

```
it.close()
next(it)
```

```
import itertools
it1 = zigzag(5)
it2 = itertools.islice(it1, 0, 20)
list(it2)
it2 = itertools.islice(it1, 1, 20)
list(it2)
it2 = itertools.islice(it1, 0, 20, 2)
list(it2)
```

