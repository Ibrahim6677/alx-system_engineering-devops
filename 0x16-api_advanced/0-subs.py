#!/usr/bin/python3

"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests
import time

def number_of_subscribers(subreddit):
	u_agent = 'Mozilla/5.0'
	headers = {'User-Agent': u_agent}
	url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
	res = requests.get(url, headers=headers, allow_redirects=False)
	if res.status_code != 200:
		return 0
	time.sleep(1)  # add a 1-second delay to avoid rate limiting
	dic = res.json()
	if 'data' not in dic:
		return 0
	if 'subscribers' not in dic.get('data'):
		return 0
	return res.json()['data']['subscribers']

subreddit = "python"  # replace with the subreddit you want to query
print(number_of_subscribers(subreddit))
