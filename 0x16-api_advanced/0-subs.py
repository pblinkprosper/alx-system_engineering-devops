#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of subscribers for a given subreddit"""
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "My Reddit Bot"})
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return 0
