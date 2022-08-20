import pandas as pd
import requests
#import json
import datetime as dt

TOKEN="BQDJ2QNsPcCbZBhMJI1emK8u0QROsn5wdsQyYrK1GJsbGImIcOQV5PEpOu8ixTpmsbfJQ_riZjE5fpV-hzjn7PPIz0R2NFIhdm76a-zoaClUs6csnW1ZMKcxI6CcVcfsxua479KqrwEC8zKE1PycWIEgbMlbqGI3hRyVdqiLTssqt4Z5DF3e1kU9FOLYUc9VCU9wy6iScfY"
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