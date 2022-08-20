import pandas as pd
import requests
import json
import datetime as dt


TOKEN = "Your API Token"
headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {TOKEN}"
        }
'''
today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
#print(yesterday_unix_timestamp)'''

r = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?limit=50", headers = headers)
data = r.json()

song_names = []
artist_names = []
played_at_list = []
timestamps = []

for song in data["items"]:
    song_names.append(song["track"]["name"])
    artist_names.append(song["track"]["album"]["artists"][0]["name"])
    played_at_list.append(song["played_at"])
    timestamps.append(song["played_at"][0:10])

print(song_names)

songs_dict = {
    "song_name" : song_names,
    "artist_name": artist_names,
    "played_at" : played_at_list,
    "timestamp" : timestamps
    }

songs_df = pd.DataFrame(songs_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])

print(songs_df)
