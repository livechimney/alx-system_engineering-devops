#!/usr/bin/python3
"""Print the titles of the first 10 hot posts listed in the subreddit
"""
from requests import get


def top_ten(subreddit):
    """Print the titles of the first 10 hot
    posts listed in the subreddit
    """

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    results = response.json().get('data')
    {print(c.get('data').get('title')) for c in results.get('children')}
