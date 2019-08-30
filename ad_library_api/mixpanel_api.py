"""
Set env vars:

export MIXPANEL_PROJECT_TOKEN=<value>
"""
import os

from mixpanel import Mixpanel

PROJECT_TOKEN = os.environ.get('MIXPANEL_PROJECT_TOKEN')

mp = Mixpanel(PROJECT_TOKEN)

# create user
user_id = "user_id_1234"
mp.people_set(user_id, {
    '$first_name': 'Leo',
    '$last_name': 'Celis',
    '$email': 'leo@leocelis.com',
    'Favorite Color': 'blue'
}, meta={'$ignore_time': 'true', '$ip': 0})

# track jump event
mp.track(user_id, 'Jump', {
    'High': '10m',
    'Surface': 'plain'
})

# track revenue
mp.people_track_charge(user_id, 999.99)
