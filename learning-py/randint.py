import random

# or
# from random import randint

rand = random.randint(0, 1)

if rand == 0:
    print("Heads")
else:
    print("Tails")

tweet_string = input("Enter your tweet: ")
tweet_string_length = len(tweet_string)

if tweet_string_length <= 30:
    print(f"Your tweet is {tweet_string_length} characters long.")
else:
    print(
        f"Your tweet is {tweet_string_length} characters long which is {tweet_string_length - 30} characters too long.")
