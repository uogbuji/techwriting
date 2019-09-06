

```
resp = go_async(access_site())
resp.status
resp.headers['Content-Type']
resp.headers['Content-Length']
```

```
url = 'http://artscene.textfiles.com/information/page_text = go_async(fetch_page(url))
page_text[:50]```

```
fetch_two = asyncio.gather(
    fetch_page('http://artscene.textfiles.com/information/ascii-newmedia.txt'),
    fetch_page('http://web.textfiles.com/computers/linux.txt')
)
resp = go_async(fetch_two)
type(resp)
resp[0][:50]
resp[1][:50]
```

```
```

```
```

```
```

```
```

