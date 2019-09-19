#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit.
        If an invalid subreddit is given, return 0.
    """
    user = {"User-Agent": "Scoot"}
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=user)
    if req.status_code != requests.codes.OK:
        return 0

    else:
        return req.json().get("data").get("subscribers")
