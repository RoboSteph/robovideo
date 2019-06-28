#Stephanie Simpler
#5-25-2019
#Getting video info from Twitch
#note - First request gets 20 most recent videos from the list (first 'page'). Next request uses the returned cursor to get older videos (second 'page').
#TODO - currently covers two pages because our videos haven't reached three pages yet

import requests
import json


f = open("info.config", "r")
l = f.readlines()
uid = l[0].rstrip()
client_id = l[1].rstrip()

url = "https://api.twitch.tv/helix/videos?user_id=" + uid
headers = {"Client-ID" : client_id}

def print_list():
    r = requests.get(url, headers=headers)
    video_dict = r.json()

    # print(video_dict)

    data_list = video_dict["data"]
    pagin = video_dict["pagination"] 
    page = pagin["cursor"]

    count = 0
    for x in data_list:
    	print(x["user_name"])
    	print(x["title"])
    	print(x["published_at"]) #Don't forget to check published_at before exporting, 24 hours or older
    	print(x["duration"])
    	print("-------------------------------------------------------------")
    	count +=1
    print("-----")
    print("Count for this page: " + str(count))
    print("-----")

    return page

url = url + "&after=" + print_list()

# print(url)

print_list()

# print(page)

# print(video_dict)

