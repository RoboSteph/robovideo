#Stephanie Simpler
#5-25-2019
#Getting video info from Twitch
#note - First request gets 20 most recent videos from the list, next request picks up where that left off
#TODO - pull user and client id from file   


import requests
import json

url = "https://api.twitch.tv/helix/videos?user_id=102812161"
headers = {"Client-ID" : "cglhpp9jnvcuzlk6gppqfya9t56u40"}

def print_list():
    r = requests.get(url, headers=headers)
    video_dict = r.json()

    data_list = video_dict["data"]
    pagin = video_dict["pagination"] 
    page = pagin["cursor"]

    count = 0
    for x in data_list:
    	print(x["user_name"])
    	print(x["title"])
    	print(x["published_at"]) #Don't forget to check published_at before exporting!
    	print(x["duration"])
    	print("-------------------------------------------------------------")
    	count +=1
    print("Count for this page: " + count)

    return page

url = url + "&after=" + print_list()

# print(url)

print_list()

# print(page)

# print(video_dict)

