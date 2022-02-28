import os
import praw
from praw.models import MoreComments
from dotenv import load_dotenv


class ThreadParser:
    """ A class to parse Reddit comments
    Attributes
    ----------
    reddit : Reddit
        Creates connection to Reddit
    comments : dict
        Holds comment information
    """

    def __init__(self):
        load_dotenv()

        self.reddit = praw.Reddit(
            client_id=os.getenv("APP_ID"),
            client_secret=os.getenv("APP_SECRET"),
            user_agent=os.getenv("USER_AGENT")
        )

        self.comments = {
        "ids": [],
        "bodies": [],
        "times": []
        }


    def get_comments(self, thread_url) -> dict:
        """ Parses all parent level comments in a given thread
        :param thread_url: url to a thread
        :type thread_url: str
        :rtype dict
        :return a dictionary of comments containing ID, body, and time
        """

        if (("https://www.reddit.com/r/" not in thread_url) or ("/comments/" not in thread_url)):
            raise ValueError("Invalid URL")

        submission = self.reddit.submission(url=thread_url)
        print(submission.title)

        # Parse all comments
        submission.comments.replace_more()
        for comment in submission.comments:
            if not isinstance(comment, MoreComments):
                self.comments["ids"].append(comment.id)
                self.comments["bodies"].append(comment.body)
                self.comments["times"].append(comment.created_utc)

        return self.comments
