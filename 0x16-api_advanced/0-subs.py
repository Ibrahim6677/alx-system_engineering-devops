#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if an error occurs.
    """
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code!= 200:
        return 0
    data = response.json()
    if 'data' not in data or 'ubscribers' not in data.get('data'):
        return 0
    return data['data']['subscribers']

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python script.py <subreddit_name>")
        sys.exit(1)
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print("The subreddit {} has {} subscribers.".format(subreddit, subscribers))
