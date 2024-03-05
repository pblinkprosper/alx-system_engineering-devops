import requests

def get_subreddit_subscribers(subreddit_name):
    """
    Queries the Reddit API and returns the total number of subscribers for a given subreddit.
    
    Args:
        subreddit_name (str): The name of the subreddit.
    
    Returns:
        int: Total number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
        response = requests.get(url, headers={"User-Agent": "My Reddit Bot"})
        data = response.json()
        return data["data"]["subscribers"]
    except (KeyError, requests.RequestException):
        return 0

