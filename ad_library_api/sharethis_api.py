"""
ShareThis - Social Share Count API
Link: https://www.sharethis.com/social-share-count-api/
"""
import ujson

from pygments import highlight, lexers, formatters

import requests

# ShareThis API endpoint
sharethis_endpoint = 'https://count-server.sharethis.com/v2.0/get_counts'

# list of URLs to get social share counts
urls = ['https://www.sharethis.com',
        'https://www.youtube.com']

for u in urls:
    try:
        # send requests
        payload = {'url': u}
        r = requests.get(sharethis_endpoint, params=payload, timeout=(5, 30))  # conn and response time
        j = r.json()

        # print response
        print("\nSocial Share Count for {}".format(u))
        formatted_json = ujson.dumps(j, sort_keys=True, indent=4)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)

    except requests.exceptions.RequestException as e:
        print(e)
