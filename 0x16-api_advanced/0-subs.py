#!/usr/bin/python3
"""Module for querying the Reddit API"""


def number_of_subscribers(subreddit):
    """Query the Reddit API and returns the number of subscribers
    to the subreddit. Checks for bugs such as null pointer references,
    unhandled exceptions, and more.
    """
    import requests

    if subreddit is None or not subreddit:
        return 0

    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            raise ValueError('Non-200 status code')
        data = response.json()
        if data is None or 'data' not in data:
            raise ValueError('Invalid response from server')
        return data['data'].get('subscribers')
    except AttributeError as e:
        raise TypeError('Missing attribute in response') from e
    except (TypeError, KeyError, ValueError) as e:
        raise ValueError('Invalid response from server') from e
