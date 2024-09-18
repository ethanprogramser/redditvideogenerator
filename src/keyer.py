import praw
import random

def get():

    empt_list = []

    reddit = praw.Reddit(
        client_id="xxxxxx",
        client_secret="xxxxxxx",
        password="xxxxxxx",
        user_agent="brain-norishment by u/Inevitable-Pace-2753",
        username="xxxxxxx",
    )


    post = reddit.subreddit("askreddit").random()
    
    empt_list.append(post.title)
    comments = post.comments
    for comments in comments[:2]:
        empt_list.append(comments.body)
        

    return empt_list

