# Quick notes on SearXNG

[SearXNG](https://github.com/searxng/searxng?tab=readme-ov-file) came up at an [RMAIIG](https://linktr.ee/rmaiig) meetup hosted in Boulder by Cameron Pope yesterday. It's basically meta-search, aggregating SERPS from engines such as Google, Bing, DuckDuckGo, etc., with a privacy angle of stripping tracking from URLs, cookies, etc. I'm sure I've heard of it in the past, or at least its predecssor SearX project, but for some reason I've never given it a go. With a current need in mind, I took an hour or two this morning to play around. Here are a few shared notes.

My lazy first gambit was to try some [existing, public instances](https://searx.space/) (no privacy issues for just messing about). Yeah forget that. They're all useless (invariably returning "Too Many Requests"). Luckily, it really is stupid easy to run yourself, esp if you use Docker. You'll want to update the default `settings.yml` to add `- json` to `formats:`, and you may find the `SEARXNG_DEBUG` variable a useful one to pass through Docker. I haven't done any work whittling down or tailoring individual search back ends yet.

The docs suck badly—I get a vague sense they're patchwork ported from SearX, or from something, perhaps. I just wanted to figure out how to use cURL on my local endpoint, so I could then translate that to Python code. Lots of head-scratching/banging, and not even a lot of help via StackOverflow, Reddit, etc. Here's a dumb example of the sort that would have saved me some time. Search for "rmaiig colorado", in news category, only results from the past day. Using Python to pretty up the JSON result. Feel free to use jq, or whatever:

```sh
curl "http://localhost:8888/search?q=rmaiig+colorado&categories=\!news&time_range=week&format=json" | python -m json.tool
```

Hope this helps someone else. Only after all this fiddling did I learn from Cameron that the WebUI is the best way to explore & figure out the REST API—he says the URLs are pretty faithful. Go figure I never even touched the WebUI. My predilection for cURL+API docs is a bit too clever for my own good, I guess 😆. He also 

Incidentally, part of my process of figuring out the REST API was peeking in Langchain's `SearxSearchWrapper` code. I guess a timely reminder: Never look in Langchain's code 🫣😂.

Cameron mentioned that SearXNG offers access to cached versions of lots of pages. I do wonder whether they rely on upstream for that. If so, [it might be a brief ride](https://news.ycombinator.com/item?id=39198329). Would be interesting to look in on [Dweb efforts to decentralize archive.org](https://archive.org/details/DWeb-Archive), then integrate into SearXNG.
