#!/usr/bin/python3
"""Query the Reddit API recursively and retruns a list containing
the titles of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], after=""):
    """Query the Reddit API recursively and retruns a list containing
    the titles of all hot articles for a given subreddit
    """

    import requests

    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
