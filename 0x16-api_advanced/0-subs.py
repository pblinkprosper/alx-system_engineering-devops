#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit (e.g., 'python', 'programming').

    Returns:
        int: Number of subscribers for the subreddit.
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url, headers={"User-Agent": "MyRedditBot"})
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except Exception as e:
        print(f"Error fetching data for subreddit '{subreddit}': {e}")
        return None
