import json
from msilib.schema import Directory
# from path import Path
from backend.Tweet_extractor import keywords
import bs4
import re
from bs4 import BeautifulSoup as bs
import requests
import os
from os import path
from operator import itemgetter


def get_flipkart_data(current_tweet_data):
    product_name = current_tweet_data["Sub_Category"]

    # item = input("Enter item to search : ")
    item = product_name
    link = f"https://www.flipkart.com/search?q={item}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
    page = requests.get(link)
    soup = bs(page.content, "html.parser")
    # it gives us the products searched with the key element in tweets
    for i in soup.find_all("a", href=re.compile("/p/")):
        for j in i.find_all("img", alt=True):
            url = "https://www.flipkart.com"
            url += i["href"]
            print(i.find_all("href"))
            current_tweet_data["product_image_link"] = j["src"]
            current_tweet_data["product_title"] = j["alt"]
            page = requests.get(url)
            soup = bs(page.content, "html.parser")
            x = soup.find_all("a", class_="_2whKao")
            sub_list = []
            Sub_Category = ""
            for item in x:
                sub_list.append(item.text)
            sub_list = sub_list[1:]
            sub_list = sub_list[:2]
            # sub_list list to string
            Sub_Category = " ".join(str(path + ">") for path in sub_list)
            Sub_Category = Sub_Category[:-1]
            current_tweet_data["Sub_Category"] = Sub_Category
            print(
                {
                    "image": j["src"],
                    "title": j["alt"],
                    "Flipkart_url": url,
                }
            )
            return current_tweet_data


def remove_duplicates(fetched_list):
    temp = set()
    new_list = []
    k = "Tweet_Text"
    for l in fetched_list:
        try:
            if l[k] not in temp:
                new_list.append(l)
                temp.add(l[k])
        except:
            pass
    return new_list


def remove_all_duplicates(fetched_list):
    res_list = []
    for i in range(len(fetched_list)):
        if fetched_list[i] not in fetched_list[i + 1 :]:
            res_list.append(fetched_list[i])

    return res_list


def sort_list(list_to_sort, name):
    newlist = sorted(list_to_sort, key=itemgetter(f"{name}"), reverse=True)
    return newlist


def name_dir():
    parent_dir = "./scrapped_data"
    Path = path.join(parent_dir)
    return Path


def write_json_file(dict, name):
    Dir = name_dir()
    if path.isfile(path.join(Dir, f"{name}.json")) is False:
        if not path.isdir(Dir):
            os.mkdir(Dir)
        json_object = json.dumps(dict, indent=4, separators=(",", ": "))
        with open(path.join(Dir, f"{name}.json"), "w") as file:
            file.write(json_object)
    else:
        with open(path.join(Dir, f"{name}.json")) as fp:
            list_Obj = json.load(fp)
            for d in dict:
                list_Obj.append(d)
        list_Obj1 = remove_all_duplicates(list_Obj)
        with open(f"{name}.json", "w") as json_file:
            json.dump(list_Obj1, json_file, indent=4, separators=(",", ": "))
