from fb_conn import graph, token

links = ["http://www.wikipedia.org",
         "http://www.reddit.com",
         "http://www.instagram.com",
         "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
         "https://twitter.com/linkinpark/status/888169188384100354"]

for link in links:
    args = dict()
    args["access_token"] = token
    args["id"] = link
    method = "/"
    r = graph.request(method, args)

    title = str(r['og_object']['title'])
    shares = int(r['share']['share_count'])
    shares_prettified = format(shares, "8,.0f")

    print("{} ({}): {} shares on Facebook\n".format(title, link, shares_prettified))
