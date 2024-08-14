#!/usr/bin/python3
""" Queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""


from collections import Counter


def count_words(subreddit, word_list, hot_list=[],
                after="None", word_count=Counter()):
    """ Queries the Reddit API, parses the title of all hot articles
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    import re
    import requests

    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    for title in hot_list:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                word_count[word] += 1

    if data['after']:
        return count_words(subreddit, word_list, hot_list,
                           data['after'], word_count)

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print('{}: {}'.format(word, count))

    return
