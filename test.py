import json
import time
import requests

def spotify():
    spotifyToken = "BQCtNDiiNQMjMd56y1b_Z8q99eRiyggXyYNi3PB_-ryxGy1YDdOZWbqtuNQENfSaglvuaxzR6JryuQFyP-MFRKXUwOiRLsk8YtjZqWLQvksycAdpit-H9RCxjXSoDzrw2XLJqqn27DFSifyrlJdBuTKTiy_CanrkphqxS46tdIDmIX3YhPwORF62ZW0H7nnl-UIj8wINoQHRruxthPMn2EP9_3uBBKNCEKiyeyOA3lGt3se0SIoaMxAP6C3rJx1m7xl1w69kW_FsFKon4GW3xn97"
    song_name = ""
    song_url = ""
    image_url = ""

    spotifyHeaders = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + spotifyToken
    }

    bannerbearHeaders = {
        "Authorization": "Bearer I86mZ6ItNwKoLSUJTLqs1wtt",
        "Content-Type": "application/json"
    }

    while True:
        res = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=spotifyHeaders)
        time.sleep(2)
        parsed_res = json.loads(res.content)
        item = parsed_res.get("item")
        if not (song_name == item.get("name")):
            song_name = item.get("name")
            print(song_name)
            artist = item.get("artists")[0]
            artist_name = artist.get("name")
            album = item.get("album")
            image = album.get("images")[1]
            image_url = image.get("url")
            externals = item.get("external_urls")
            song_url = externals.get("spotify")
            data = {
              "template": "gwNr4n50oxoZROMBdo",
              "modifications": [
                {
                  "name": "song_name",
                  "text": song_name,
                },
                {
                  "name": "Song_Image",
                  "image_url": image_url
                },
                {
                  "name": "song_link",
                  "target": song_url
                }
              ]
            }
            res = requests.post("https://api.bannerbear.com/v2/images", headers=bannerbearHeaders, data=json.dumps(data))
            print(res.content)
        time.sleep(2)

spotify()