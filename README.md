# Facebook_Ad_Library_API
Python code package to scrape the Facebook Ad Library data

Who Targets Me have open-sourced this scraping package to make it easier for researchers to scrape the Facebook Ad Library, even if you have a limited knowledge of python.

See basic steps here or email contact@whotargets.me for any additional guidance:

Download Zip

Download Python3/Anaconda distribution
https://www.anaconda.com/distribution/

Get Facebook Ad Library access token permissions (need to send I.d. and wait 24 hours for approval)
https://www.facebook.com/ads/library/api/

In file ensure fbconn.py is in same file as ad_scraper.py

In ad_scraper.py go through four key changes:
- # 1. Change 'countries = []' to include an ISO country code: https://www.nationsonline.org/oneworld/country_code_list.html
- # 2. Change Ad Library Access Token (args["search_terms"]), available here:  https://developers.facebook.com/tools/explorer/
- # 3. Change Ad Library (args["access_token"]) to include a search term or else do full search with '*'
- # 4. Change the final line to the folder on your computer where you want the scraped csv to appear.
