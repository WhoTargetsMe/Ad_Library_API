import ujson

from fb_conn import graph, token
from pygments import highlight, lexers, formatters

links = ["http://www.wikipedia.org",
         "http://www.reddit.com",
         "http://www.instagram.com",
         "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
         "https://twitter.com/linkinpark/status/888169188384100354",
         "http://cursosrosario.com/",
         "http://blog.leocelis.com/2019/01/15/using-ai-to-understand-the-customers-journey/"]

for link in links:
    args = dict()
    args["access_token"] = token
    args["id"] = link
    args["metadata"] = 1
    method = "/"
    r = graph.request(method, args)
    formatted_json = ujson.dumps(r, sort_keys=True, indent=4)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)
