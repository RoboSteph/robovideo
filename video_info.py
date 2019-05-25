#Stephanie Simpler
#5-25-2019
#Getting video info from Twitch
#note - currently only showing 20 videos in the list


import requests
import json

url = "https://api.twitch.tv/helix/videos?user_id=102812161"
headers = {"Client-ID" : "cglhpp9jnvcuzlk6gppqfya9t56u40"}


r = requests.get(url, headers=headers)
video_dict = r.json()

data_list = video_dict["data"]

count = 0

for x in data_list:
	print(x["user_name"])
	print(x["title"])
	print(x["published_at"]) #Don't forget to check published_at before exporting!
	print(x["duration"])
	print("-------------------------------------------------------------")
	count +=1

print(count)


# {'id': '429360909', 'user_id': '102812161', 'user_name': 'RoboSteph', 'title': 'Apex', 'description': '', 'created_at': '2019-05-24T21:59:55Z', 'published_at': '2019-05-24T21:59:55Z', 'url': 'https://www.twitch.tv/videos/429360909', 'thumbnail_url': 'https://static-cdn.jtvnw.net/s3_vods/7a7e93b6ab17ad0908b4_robosteph_34252272320_1209429564/thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 0, 'language': 'en', 'type': 'archive', 'duration': '8h26m36s'} 

#Get id from username
#curl -H "Client-ID: cglhpp9jnvcuzlk6gppqfya9t56u40" -X GET "https://api.twitch.tv/helix/users?login=robosteph"

#Get videos 
#curl -H "Client-ID: cglhpp9jnvcuzlk6gppqfya9t56u40" -X GET "https://api.twitch.tv/helix/videos?user_id=102812161"