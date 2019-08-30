from tw_conn import twitter

MAX_ATTEMPTS = 10


def get_tweets(topics_list: list, lang: str = "en", count: int = 100) -> list:
    """
    Return tweets for a given topic

    :param topics:
    :param lang:
    :param count:
    :return:
    """

    tweets = []
    next_max_id = 0

    for topic in topics_list:
        print("\nRetrieving tweets for topic {}".format(topic))

        for i in range(0, MAX_ATTEMPTS):

            if count < len(tweets):
                break

            # STEP 1: Query Twitter
            if i == 0:
                # Query twitter for data.
                results = twitter.search(q=topic, lang=lang, count='100')
            else:
                # After the first call we should have max_id from result of previous call. Pass it in query.
                results = twitter.search(q=topic, lang=lang, include_entities='true', max_id=next_max_id)

            # STEP 2: Save the returned tweets
            for result in results['statuses']:
                tweets.append(result)

            # STEP 3: Get the next max_id
            try:
                # Parse the data returned to get max_id to be passed in consequent call.
                next_results_url_params = results['search_metadata']['next_results']
                next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
            except:
                # No more next pages
                break

            print("\nTweets found: {}".format(len(tweets)))

    return tweets


def get_most_retweeted(tweets: list) -> dict:
    """
    For a given list of tweets, return the most retweeted

    :param tweets:
    :return:
    """
    rc = 0
    tt = ""

    print("\nTweets found: {}".format(len(tweets)))

    for t in tweets:

        retweets = t['retweet_count']

        # print("\n Tweet: {} - Retweets: {}".format(format_tweet_url(tweet=t), retweets))

        if retweets > rc:
            rc = retweets
            tt = t

    return tt


def format_tweet_url(tweet: dict) -> str:
    """
    Construct tweet link url

    :param tweet:
    :return:
    """
    tweet_url = "https://twitter.com/{}/status/{}".format(tweet['user']['screen_name'],
                                                          tweet['id_str'])

    return tweet_url


# 1. Select a topic
topics = ["#DigitalMarketing", "#SMM", "#SEO", "#Contentmarketing", "#GrowthHacking",
          "#SocialMediaMarketing", "#Onlinemarketing", "#Emailmarketing", "#Videomarketing",
          "#adtech", "#martech", "#growthmarketing"]

# 2. Get last X tweets
tweets = get_tweets(topics_list=topics, count=10000)

# 3. Get the most retweeted
top_retweeted = get_most_retweeted(tweets=tweets)

# 4. Print the winner
print("\n\nMost retweeted: {} - Retweets: {}"
      "\n".format(format_tweet_url(tweet=top_retweeted),
                  top_retweeted['retweet_count']))
