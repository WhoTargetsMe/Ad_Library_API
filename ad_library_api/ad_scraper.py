#Code by Roland Adorjani @RolandAdorjani

from fb_conn import graph, token
from pygments import highlight, lexers, formatters

import pandas as pd

from urllib.parse import urlsplit, parse_qs

import os

countries =['GB']

# Four changes are neeeded to use this code:
# 1. Change 'countries = []' to ISO country code: https://www.nationsonline.org/oneworld/country_code_list.html
# 2. Change Ad Library Access Token (args["search_terms"]), available here:  https://developers.facebook.com/tools/explorer/
# 3. Change Ad Library (args["access_token"]) search term or else do full search with *
# 4. Change this to the folder on your computer where you want the scraped csv to appear

# formatted_json = ujson.dumps(r, sort_keys=True, indent=4)
# colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
# print(colorful_json)

def build_args(url=None):


    for k, v in args.items():
        args[k] = v

    if url:
        query = urlsplit(url).query
        params = parse_qs(query)
        for k, v in params.items():
            args[k] = v[0]

    return args




for country in countries:
	args = dict()
	args["access_token"] = 'EAAE5X3NWzjUBAKT3FJBh1NxTqgiNVzngeYqtPtti8QY38oOMKFFrDCXfMC8RW5e0K2PFJEaMvaM2lZBWUdBMtA4acvs4fZC3EGyyhkIZCfGySYdPRvvMFPeMT6Pk00qeLrqikL3HH8XgRDxusF6ZAPWFvyLjXUbqxb5O8xX8EN9ZBhHGLtpJBqEsgsYxMsBbR2o3nZCMmxDgZDZD'
	args["search_terms"] = '*'
	args["ad_type"] = 'POLITICAL_AND_ISSUE_ADS'
	args["ad_reached_countries"] = [country]
	args['ad_active_status'] = 'ALL'
	args["fields"] =  'ad_creation_time,ad_delivery_start_time,ad_delivery_stop_time,ad_creative_body,ad_creative_link_caption,ad_creative_link_title,ad_creative_link_description,ad_snapshot_url,currency,funding_entity,demographic_distributio,impressions,page_id,page_name,region_distribution,spend'
	method = "/ads_archive"

	dfs = []
	# r = graph.request(method, args)
	r = graph.request(method, args)
	dfs.append(pd.DataFrame(r.get('data', [])))


	i=0
	next_page = r.get('paging', {}).get('next')
	print(next_page)
	while next_page!=None:


	    try:
	        # get next page
	        args = build_args(url=next_page)
	        r = graph.request(method, args)
	        next_page = r.get('paging', {}).get('next')

	        dfs.append(pd.DataFrame(r.get('data', [])))

	        i+=1
	        print(i)
	    except:
	        pass
	df = pd.concat(dfs)


	df = pd.concat([df.drop(['impressions'], axis=1), df['impressions'].apply(pd.Series)], axis=1)
	df.rename(columns={'lower_bound': 'lower_bound_impressions', 'upper_bound': 'upper_bound_impressions'}, inplace=True)


	df.to_csv('/Users/rachel/desktop/BBC/brexitparty.csv'.format(country), encoding='utf8')
