# Facebook_Ad_Library_API
Python code package to scrape the Facebook Ad Library data

Who Targets Me have open-sourced this scraping package to make it easier for researchers to scrape the Facebook Ad Library, even if you have a limited knowledge of python.

See basic steps here or email contact@whotargets.me for any additional guidance:

1. Download ad_library_api Zip

2. Download Python/Anaconda distribution (version 3.7)
https://www.anaconda.com/distribution/
See how to set up anaconda enviroment on your PC here: https://docs.anaconda.com/anaconda/user-guide/getting-started/

3. Get Facebook Ad Library access token permissions (need to send I.d. and wait 24 hours for approval)
https://www.facebook.com/ads/library/api/

4. In file ensure fbconn.py is in same folder as ad_scraper.py
If you receive the error "fbconn.py is not found" simpy add the below code to the 'import' section of the fbconn.py file:
"import sys
sys.path.insert(1, 'C:/Users/"user name"/Anaconda3/envs/"your anaconda environment"/Lib/site-packages')
import facebook

In ad_scraper.py go through four key changes:
- # 1. Change 'countries = []' to include an ISO country code: https://www.nationsonline.org/oneworld/country_code_list.html
- # 2. Change Ad Library Access Token (args["search_terms"]), available here:  https://developers.facebook.com/tools/explorer/
- # 3. Change Ad Library (args["access_token"]) to include a search term or else do full search with '*'
- # 4. Change the final line to the folder on your computer where you want the scraped csv to appear.
