import sys
import getopt
import tweepy
import configparser
import csv


def main():
    argv = sys.argv[1:]

    try:
        opts, _ = getopt.getopt(argv, "s:f:", ["screen_name=", "file="])
        for opt, arg in opts:
            if opt in ["-s", "--screen_name"]:
                block_user(arg)
            elif opt in ["-f", "--file"]:
                read_file(arg)
    except:
        print("error")


def read_file(file_name):
    try:
        with open(file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                block_user(row[0])
    except ValueError as e:
        print(e)


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
