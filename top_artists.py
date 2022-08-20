import pandas as pd
import requests
#import json
import datetime as dt

TOKEN="Your API Token"
headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {TOKEN}"
        }

r = requests.get("https://api.spotify.com/v1/me/top/artists?limit=11", headers = headers)
data = r.json()
print(data["items"])

artist_names = []
genres = []
popularity = []

for artist in data["items"]:
    artist_names.append(artist["name"])
    popularity.append(artist["popularity"])
    genres.append(artist["genres"])

print(artist_names)

artist_dict = {
    "Artist Name" : artist_names,
    "Popularity": popularity,
    "Genres" : genres
    }

artist_df = pd.DataFrame(artist_dict, columns = ["Artist Name", "Popularity", "Genres"])
print("******************************************************************************")
print("                         Your TOP ARTISTS!!! are                              ")
print("******************************************************************************")
print(artist_df)
