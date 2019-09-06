

```
mylist = [ ix for ix in range(10, 20) ]
print(mylist)
mylist = [ c.upper() for c in 'Hello, world!' if c.isalpha() ]
mylist
```

```
mylist = [ (i, j) for i in range(0, 3) for j in range(10, 13) ]
mylist
[(0, 10), (0, 11), (0, 12), (1, 10), (1, 11), (1, 12), (2, 10), (2, 11), (2, 12)]
mylist = [ i * j for i in range(0, 3) for j in range(10, 13) ]
mylist
```

```
mygen = ( ix for ix in range(10, 20) )
print(mygen)
print(next(mygen))
```

```
s = 'hello world and everyone in the world'
subs = {'hello': 'goodbye', 'world': 'galaxy'}
for word in substituter(s.split(), subs):
    print(word, end=' ')
```

```
import math
notby2or3 = (
    n for n in range(1, 20) if math.gcd(n, 2) == 1 and math.gcd(n, 3) == 1
)
print(list(notby2or3))
```

```
notby2or3 = (
    n for n in range(1, 20) if math.gcd(n, 2) == 1 and math.gcd(n, 3) == 1
)
squarednotby2or3 = ( n*n for n in notby2or3 )
print(list(squarednotby2or3))
```

```
r = range(10)
m = map(str, r)
next(m)
list(m)
```

```
def get_letter(i):
    return chr(ord('a')+i)
r = range(10)
list(map(get_letter, r))
```

```
list( ( get_letter(i) for i in range(10) ) )

list( ( chr(ord('a')+i) for i in range(10) ) )
```

```
import math
def notby2or3(n):
    return math.gcd(n, 2) == 1 and math.gcd(n, 3) == 1
list(filter(notby2or3, range(1, 20)))
```

```
sum(range(20, 30))

def sum_of_squares(acc, i):
    return acc + i**2

import functools
functools.reduce(sum_of_squares, range(10))
```


```
tenletters = ( chr(ord('a')+i) for i in range(10) )
'!'.join(tenletters)
'!'.join(tenletters)
tenletters = ( chr(ord('a')+i) for i in range(10) )
''.join(tenletters)
tenletters = ( chr(ord('a')+i) for i in range(10) )
' and '.join(tenletters)
```

```

```


```

```

