import sys
import getopt
import tweepy
import configparser


def main():
    screen_name = None
    argv = sys.argv[1:]

    try:
        opts, _ = getopt.getopt(argv, "s:", ["screen_name="])
        for opt, arg in opts:
            if opt in ["-s", "--screen_name"]:
                screen_name = arg

        block_user(screen_name)
    except:
        print("error")


def block_user(screen_name):
    try:
        # fetch values from config file
        parser = configparser.ConfigParser()
        parser.read("application.ini")

        consumer_key = parser['Twitter']['consumer_key']
        consumer_secret = parser['Twitter']['consumer_secret']
        access_token = parser['Twitter']['access_token']
        access_secret = parser['Twitter']['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        api.report_spam(screen_name=screen_name)
    except tweepy.TweepError as e:
        print(e)


if __name__ == "__main__":
    main()
