from twython import Twython

APP_KEY = 'z1eaXOkhh2aiTjJnSzO0aeHZV'
APP_SECRET = 'cDA5wSxV0B2VA2R07DZXcXpchfRhWFWhGlYiQH556ZCuRvfDB7'

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
