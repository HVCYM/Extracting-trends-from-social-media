from pyparsing import FollowedBy
# from sqlalchemy import true
from tomli import load
import tweepy
from . import scrape_data as sd
import pandas as pd

# from dotenv import load_dotenv
import os
import backend.keys as key
# from dotenv import load_dotenv
# load_dotenv()

consumer_key = key.consumer_key
consumer_secret = key.consumer_secret
access_token = key.access_token
access_token_secret = os.getenv(key.access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

from backend.Tweet_extractor import keywords 


Electronics_Keywords = [ keywords.Electronics_Keywords ]

Shoes_Keywords = [ keywords.Shoes_Keywords ]
Fashion_Keywords = [    keywords.Fashion_Keywords ]
Phones_keywords = [   keywords.Phones_keywords ]

# number of tweets to fetch
number_of_tweets_to_extract = 100

def electronics(name="Electronics"):
    print("oh yeah")
    Electronics_List = [
        "#computers",
        "#tech",
        "#innovation",
        "laptops",
        " #Technology",
        "gbs_systems",
        "#laptops",
        "Delllaptop",
        "Laptop Mag",
        "hplaptop",
        "avitalaptop",
        "iball laptop",
    ]
    Electronics_tweet = []
    count = 0
    for electronic in Electronics_List:
        tweets_electronics = tweepy.Cursor(
            api.search_tweets,
            electronic,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_electronics:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                # Inserting hashtags in hash_list
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            # searching for the product name in the tweet
            flag = False
            line["Brand"] = "null"
            try:
                for i in Electronics_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        # Full_name = i.split(" ")
                        # line["main_category"] = name
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        # for j in line["hashtags_Tweet_Text"]:
                        flag = True
                        Full_name = i.split(" ")
                        # line["main_category"] = name
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag == True:
                    Electronics_tweet.append(line)
                    # print("Tweet Accepted according to requirements")
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Electronics_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Electronics_tweet)
    if len(Electronics_tweet) == 0:
        return
    Electronics_tweet = sd.remove_duplicates(Electronics_tweet)
    new_Electronics_tweet = sd.sort_list(Electronics_tweet, "Trend_score")
    sd.write_json_file(new_Electronics_tweet, f"{name}")


def shoes(name="Shoes"):
    Shoes_List = [
        "paragonfootwear",
        "FluoShoes",
        "Batakenya",
        "RedTapeindia",
        "LakhaniFootwear",
        "metroshoes",
        "dvsshoes",
        "#shoes",
        "J23app",
    ]
    Shoes_tweet = []
    count = 0
    for shoes in Shoes_List:
        tweets_Shoes = tweepy.Cursor(
            api.search_tweets,
            shoes,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_Shoes:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Shoes_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag:
                    Shoes_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Shoes_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Shoes_tweet)
    if len(Shoes_tweet) == 0:
        return
    Shoes_tweet = sd.remove_duplicates(Shoes_tweet)
    new_Shoes_tweet = sd.sort_list(Shoes_tweet, "Trend_score")
    sd.write_json_file(new_Shoes_tweet, f"{name}")


def fashion(name="Fashion"):
    Fashion_List = [
        "#fashion",
        "#handbags",
        "@refinery29",
        "#Sunglasses",
        "asimjofa",
        "Ezpopsy",
        "StingClothing",
        "casualclassics",
        "#jeans",
    ]
    Fashion_tweet = []
    count = 0
    for fashion in Fashion_List:
        tweets_fashion = tweepy.Cursor(
            api.search_tweets,
            fashion,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_fashion:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Fashion_Keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag == True:
                    Fashion_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Fashion_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Fashion_tweet)
    if len(Fashion_tweet) == 0:
        return
    Fashion_tweet = sd.remove_duplicates(Fashion_tweet)
    new_Fashion_tweet = sd.sort_list(Fashion_tweet, "Trend_score")
    sd.write_json_file(new_Fashion_tweet, f"{name}")


def phones(name="Phones"):
    Phone_List = [
        "91mobiles",
        "techdroider",
        "techylogy",
        "#iphone",
        "#newphone",
        "#watchestobuy",
    ]
    Phone_tweet = []
    count = 0
    for phone in Phone_List:
        tweets_phones = tweepy.Cursor(
            api.search_tweets,
            phone,
            tweet_mode="extended",
            lang="en",
            include_entities=True,
        ).items(number_of_tweets_to_extract)
        tweet_count = 0
        for tweet in tweets_phones:
            try:
                # information of tweet
                txt = tweet.full_text
                id = tweet.id
                screen_id_name = tweet.author._json["screen_name"]
                user = api.get_user(screen_name=screen_id_name)
                follower_count = user.followers_count
                url = "https://twitter.com/twitter/statuses/" + str(id)
                likes = tweet.favorite_count
                retweet_count = tweet.retweet_count
                Trend_score = likes + retweet_count + follower_count * 0.4
                hash_list = []
                if "hashtags" in tweet.entities:
                    hashtag = tweet.entities["hashtags"]
                    for hsht in hashtag:
                        hash_list.append(hsht["text"])
                if "media" in tweet.entities:
                    for image in tweet.entities["media"][0]:
                        line = {
                            "Category": f"{name}",
                            "url": url,
                            "Tweet_Text": txt,
                            "Trend_score": Trend_score,
                            "IMAGE_URL": tweet.entities["media"][0]["media_url"],
                            "hashtags_Tweet_Text": hash_list,
                        }

                    print("Image found!")
                else:
                    line = {
                        "Category": f"{name}",
                        "url": url,
                        "Tweet_Text": txt,
                        "Trend_score": Trend_score,
                        "IMAGE_URL": "null",
                        "hashtags_Tweet_Text": hash_list,
                    }

                # Access video info
                try:
                    if "media" in tweet.entities:
                        for media in tweet.extended_entities["media"]:
                            line["video_img_url"] = media["media_url"]
                except:
                    pass
                line["id"] = id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break
            flag = False
            line["Brand"] = "null"
            try:
                for i in Phones_keywords:
                    if i in line["Tweet_Text"]:
                        flag = True
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        print(i)
                        line = sd.get_flipkart_data(line)
                        break
                    elif i in hash_list:
                        flag = True
                        Full_name = i.split(" ")
                        line["Sub_Category"] = i
                        line["Brand"] = i.split(" ")[0]
                        line = sd.get_flipkart_data(line)
                        print(i)
                        break
            except Exception as e:
                print(str(e))
            # checking if our tweet is valid or not
            try:
                if Trend_score >= 10 and flag:
                    Phone_tweet.append(line)
                else:
                    print("Tweet rejected not according to requirements")
            except:
                Phone_tweet.append(line)
            tweet_count += 1
        count = count + tweet_count
        print(count)
    print(f"Total Tweets Scraped:=> {count}")
    print(Phone_tweet)
    if len(Phone_tweet) == 0:
        return
    Phone_tweet = sd.remove_duplicates(Phone_tweet)
    updated_Phone_tweet = sd.sort_list(Phone_tweet, "Trend_score")
    sd.write_json_file(updated_Phone_tweet, f"{name}")


# electronics()
# shoes()
# fashion()
# phones()
