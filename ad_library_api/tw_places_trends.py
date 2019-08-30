from tw_conn import twitter


def get_most_trendy(woeid: int) -> dict:
    """
    Get trends with more volume in location

    :param woeid: WOEID (Where On Earth IDentifier) - http://www.woeidlookup.com/
    :return: trend object
    """
    # get location trends
    trends = twitter.get_place_trends(id=woeid)[0]['trends']

    # find the one with most volume
    mv = 0
    t = {}

    for trend in trends:
        tv = trend['tweet_volume']

        if not tv:
            continue

        if tv and tv > mv:
            mv = tv
            t = trend

    return t


def get_most_retweeted(trend: dict, count: int = 100) -> dict:
    """
    Return the most retweeted tweet for a given trend within the specified count

    :param trend: trend object
    :param count: how many results
    :return: tweet object
    """
    q = trend['query']
    results = twitter.cursor(twitter.search, q=q)

    i = 0
    mr = 0
    win = {}

    for result in results:
        tweet = twitter.show_status(id=result['id'])
        rt = tweet['retweet_count']

        if not rt:
            continue

        if rt and rt > mr:
            mr = rt
            win = tweet

        i += 1
        if i == count:
            break

    return win


# WOEID = 1  # the world...
WOEID = 2487956
trend = get_most_trendy(WOEID)
tweet = get_most_retweeted(trend)

print("\nMost trendy topic: {} \n\n".format(trend['name']))
print("\nMost relevant tweet: {} \n\n".format(tweet['text']))
