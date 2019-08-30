"""
Page Posts Insights

export PAGE_ACCESS_TOKEN=<token>
export APP_ID=<app_id>
export APP_SECRET=<secret>
export API_VERSION=<api_ver>

Get a temp token: https://developers.facebook.com/tools/explorer

Extend token: https://developers.facebook.com/tools/debug/accesstoken/

Available metrics: https://developers.facebook.com/docs/graph-api/reference/v3.2/insights#availmetrics

1. Get all the posts
2. Save them in memory
3. Find the post with most reach
4. Find the post with more shares

"""
import os
from time import sleep
from urllib.parse import urlsplit, parse_qs

from fb_conn import graph

# facebook page
path = "/139393722802931/posts"

posts = list()


def build_args(url=None, **kwargs):
    args = dict()
    args["access_token"] = os.environ.get('PAGE_ACCESS_TOKEN')

    for k, v in kwargs.items():
        args[k] = v

    if url:
        query = urlsplit(url).query
        params = parse_qs(query)
        for k, v in params.items():
            args[k] = v[0]

    return args


# get posts
args = build_args(limit=100)
r = graph.request(path, args)

next_page = r.get('paging', {}).get('next')
while next_page:
    # add current posts
    posts.append(r.get('data', []))

    # get next page
    args = build_args(url=next_page)
    r = graph.request(path, args)
    next_page = r.get('paging', {}).get('next')

    print("Getting new page {}\n".format(next_page))

    sleep(1)
    break

for pl in posts:
    for p in pl:
        # get post insights
        print(p)
        exit()

        # TODO: get the link
        # TODO: then get the shares from graph api (fb_link_shares)

        # post_id = p.get('id').split("_")[1]
        post_id = p.get('id')
        method = "{}/insights".format(post_id)
        metrics = "post_activity,post_activity_unique,post_activity_by_action_type," \
                  "post_activity_by_action_type_unique,post_clicks,post_clicks_unique," \
                  "post_clicks_by_type,post_clicks_by_type_unique,post_impressions_unique," \
                  "post_impressions_paid,post_impressions_paid_unique,post_impressions_fan,post_impressions_fan_unique," \
                  "post_impressions_fan_paid,post_impressions_fan_paid_unique,post_impressions_organic," \
                  "post_impressions_organic_unique,post_impressions_viral,post_impressions_viral_unique," \
                  "post_impressions_nonviral,post_impressions_nonviral_unique,post_impressions_by_story_type," \
                  "post_impressions_by_story_type_unique,post_engaged_users,post_negative_feedback," \
                  "post_negative_feedback_unique,post_negative_feedback_by_type,post_negative_feedback_by_type_unique," \
                  "post_engaged_fan,post_clicks,post_clicks_unique,post_clicks_by_type,post_clicks_by_type_unique," \
                  "post_reactions_like_total,post_reactions_love_total,post_reactions_wow_total," \
                  "post_reactions_haha_total,post_reactions_sorry_total,post_reactions_anger_total," \
                  "post_reactions_by_type_total"
        metrics = "post_activity"
        # r = graph.request(method, build_args(metric=metrics, period="lifetime"))
        # r = graph.request(method, build_args(metric=metrics))
        method = "{}/reactions".format(post_id)
        r = graph.request(method, build_args())

        print("Post ID {} - Activity: {} \n".format(post_id, r.get('data')))

    sleep(1)
