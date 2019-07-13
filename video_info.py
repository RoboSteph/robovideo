#Stephanie Simpler
#5-25-2019
#Getting video info from Twitch

import requests
import json

class VideoInfo(): 

	def __init__(self, uid, client_id, url):
		self.uid = uid #remove this?
		self.client_id = client_id
		self.url = url
		self.headers = {"Client-ID" : client_id}

	def print_list(self):
	    r = requests.get(self.url, headers = self.headers)
	    video_dict = r.json()
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

	    return count, page


f = open("info.config", "r")
l = f.readlines()
uid = l[0].rstrip()
client_id = l[1].rstrip()
url = "https://api.twitch.tv/helix/videos?user_id=" + uid

e = VideoInfo(uid, client_id, url)

vid_count, p = e.print_list()

while vid_count >= 20: 
	e.url = url + "&after=" + p
	vid_count, p = e.print_list()