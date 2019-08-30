import ujson

from fb_conn import graph, token
from pygments import highlight, lexers, formatters

args = dict()
args["access_token"] = token
args["search_terms"] = 'california'
args["ad_type"] = 'POLITICAL_AND_ISSUE_ADS'
args["ad_reached_countries"] = ['US']
args["fields"] = 'ad_creation_time'
method = "/ads_archive"
r = graph.request(method, args)
formatted_json = ujson.dumps(r, sort_keys=True, indent=4)
colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
print(colorful_json)
