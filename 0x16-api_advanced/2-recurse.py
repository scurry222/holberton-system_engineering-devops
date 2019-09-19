#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[]):
    """ Prints the titles of an amount of hot posts
        listed for a given subreddit.
        solve with recursion, by using the 'after' request.
    """
    user = {"User-Agent": "Scoot"}
    if len(hot_list) is 0:
        req = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers=user)
    else:
        req = requests.get("https://www.reddit.com/r/{}/hot.json?after={}_{}"
                           .format((subreddit),
                                   hot_list[-1].get('kind'),
                                   hot_list[-1].get('data').get('id')),
                           headers=user)
    if req.status_code != requests.codes.OK:
        return None
    if len(req.json().get('data').get('children')) < 1:
        return hot_list
    hot_list.extend(req.json().get('data').get('children'))
    return recurse(subreddit, hot_list)
