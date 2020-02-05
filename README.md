# Facebook_Ad_Library_API

🚨 **This library has been superceded internally, so we won't be maintaining it any further.** 🚨

**Thank you everyone who has contributed.**

### Scraping

Created by Roland Adorjani @RolandAdorjani

Python code package to scrape the Facebook Ad Library data

Who Targets Me have open-sourced this scraping package to make it easier for researchers to scrape the Facebook Ad Library, even if you have a limited knowledge of python.

See basic steps here or email contact@whotargets.me for any additional guidance:

1. Download ad_library_api Zip

2. Download Python/Anaconda distribution (version 3.7)
   https://www.anaconda.com/distribution/
   See how to set up anaconda enviroment on your PC here: https://docs.anaconda.com/anaconda/user-guide/getting-started/

3. Get Facebook Ad Library access token permissions (need to send I.d. and wait 24 hours for approval)
   https://www.facebook.com/ads/library/api/

4) In ad_scraper.py go through four key changes:

- A. Change 'countries = []' to include an ISO country code: https://www.nationsonline.org/oneworld/country_code_list.html
- B. Change (args["access_token"] = 'insert') to insert Ad Library Access Token, available here: https://developers.facebook.com/tools/explorer/
- C. Change Ad Library (args["search_terms"] = 'insert') to insert a search term or else do full search with '\*'
- D. Change the final line to the folder on your computer where you want the scraped csv to appear.
- E. If you would like to change the range of the scrape, you can change the number of 'pages' the code scrapes here:

  `i=0 next_page = r.get('paging', {}).get('next') print(next_page) for i in range(100):`

  Or else to scrape every possible page since the ad library began (particularly if you just want to search a term) use this code instead:

  `i=0 next_page = r.get('paging', {}).get('next') print(next_page) for i in range(100):`

5. In your terminal command line, locate the ad_library_api folder and run the ad_scaper.py file

- "python3 ad_scraper.py"

If you receive the error "fbconn.py is not found" when you run the file
A. In file ensure fbconn.py is in same folder as ad_scraper.py
B. If persists, find out where facebook package is located with: pip show facebook-sdk
C. Add the below code to the 'import' this file location into the 'import' section of the fbconn.py file
ie.

import sys
sys.path.insert(1, 'C:/Users/"insert PC user"/Anaconda3/envs/"insert your anaconda environment"/Lib/site-packages')
import facebook"

### Parsing

Created by Felix Szabo @fgszabo

Jupyter code package to clean the API csv (needed to lay out the demographic string into multiple columns based on gender and age breakdown)

In the terminal command line open Jupyter

'jupyter notebook'

Select WTM_Data_Gender_basic.ipynb and adapting the code

- In[2]: Change the location/name of the source file
- In [4]: Change the date range you wish to parse
- In [15]: Change the name of the final file.

Run each line and final file will save to your desktop.
