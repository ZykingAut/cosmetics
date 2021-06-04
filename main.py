import textwrap
import urllib.request
import os

from dotenv import load_dotenv
from labypy import Halo, Dragon, Wings, Fisher, Hand, Cape, Eyes, Horns
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from threading import Thread
from PIL import Image, ImageDraw, ImageFont, ImageColor

load_dotenv()
cookie = os.getenv("LABYMOD_COOKIE")

halo = Halo.Instance(cookie)
dragon = Dragon.Instance(cookie)
wings = Wings.Instance(cookie)
fisher = Fisher.Instance(cookie)
hand = Hand.Instance(cookie)
eyes = Eyes.Instance(cookie)
horns = Horns.Instance(cookie)
cape = Cape.Instance(cookie)

interval = 75

dragons = {
    "ender": "17802074-54e6-43a9-8591-8602ec3366c8,1",
    "night": "238c7d0f-05a8-49fc-8884-e990c5c2eea8,1",
    "ocean": "24677cb1-7de2-4114-bd4b-fc7174c8cdfa,1",
    "desert": "488a2b9f-1a6a-4669-8be1-d991147b29e4,1",
    "fire": "5b5bb9fa-da66-4dff-b53f-c598f0a4c173,1",
    "sunset": "70ded070-5709-4893-a28a-bba009faec7e,1",
    "pitaya": "89b9bdbc-1177-497d-ac8f-d72acd42a84f,1",
    "sun": "8c67c2b0-719e-4736-a305-579f42f6886d,1",
    "lavender": "8ea568f4-3c33-4cb1-9dbe-603b66b49185,1",
    "snow": "aa26b30f-7761-4f54-ba34-93803f515b97,1",
    "water": "b363ac4f-45f4-46c4-9483-11eb57054b16,1",
    "smoke": "cccd8d73-4d5f-4c85-9482-96911c713778,1",
    "plant": "ebbe1177-5d07-419d-bba1-fb23140312e0,1",
}


def cape_border(color):
    cape_width = 355
    cape_img = Image.open("cape.png")
    border = ImageDraw.Draw(cape_img)
    border.line(((25, 25), (25, 265), ((cape_width // 2) - 10, 265), ((cape_width // 2) - 10, 25), (25, 25)),
                fill=ImageColor.getrgb("#" + color.get()), width=3)
    cape_img.save("cape.png")
    time.sleep(1)


def create_cape(song_name, author_name):
    cape_width = 355
    cape_height = 275
    spotify_img = Image.open("spotify.png", "r")
    spotify_img_resized = spotify_img.resize((125, 125))
    cape_img = Image.new('RGBA', (355, 275), (0, 0, 0, 255))
    offset = (((cape_width // 2) - 110) // 2, 45)
    cape_img.paste(spotify_img_resized, offset)
    song_font = ImageFont.truetype("AmaticSC-Bold.ttf", 26)
    author_font = ImageFont.truetype("AmaticSC-Regular.ttf", 18)
    song_info = ImageDraw.Draw(cape_img)
    lines = textwrap.wrap(song_name, width=16)
    song_name_height = cape_height - 87
    if len(song_name) >= 32:
        song_font = ImageFont.truetype("AmaticSC-Bold.ttf", 20)
        lines = textwrap.wrap(song_name, width=20)
    for line in lines:
        line_width, line_height = song_font.getsize(line)
        if len(song_name) <= 16:
            song_info.text(((cape_width // 2) // 2 + 10, song_name_height + 10), line, fill="white", font=song_font,
                           anchor="mm")
        elif len(song_name) >= 32:
            song_info.text(((cape_width // 2) // 2 + 10, song_name_height - 10), line, fill="white", font=song_font,
                           anchor="mm")
        else:
            song_info.text(((cape_width // 2) // 2 + 10, song_name_height), line, fill="white", font=song_font,
                           anchor="mm")
        song_name_height += line_height
    if len(song_name) >= 32:
        song_name_height -= 10
    elif len(song_name) <= 16:
        song_name_height += 10
    song_info.text(((cape_width // 2) // 2 + 10, song_name_height), author_name, fill="white", font=author_font,
                   anchor="mm")
    cape_img.save("cape.png")
    time.sleep(1)


def get_spotify_stuff(song):
    song = song.get("item")
    song_name = song.get("name")
    album = song.get("album")
    artist = song.get("artists")[0]
    artist_name = artist.get("name")
    image_data = album.get("images")[1]
    image_url = image_data.get("url")
    urllib.request.urlretrieve(image_url, "spotify.png")
    song_name = str(song_name).split("(feat.")[0]
    if song_name == "Rauch":
        song_name = "Vani"
    return song_name, artist_name


def spotify_cloak():
    print("Cloak Thread Started")
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), requests_timeout=10, status_retries=3)
    last_song_id = ""
    while True:
        current_song = sp.currently_playing()
        if current_song is not None:
            # print(current_song)
            if current_song.get("timestamp") != 0:
                song = current_song.get("item")
                current_song_id = song.get("id")
                # print(current_song_name)
                if not current_song_id == last_song_id:
                    # print(current_song_name)
                    last_song_id = current_song_id
                    song_name, author_name = get_spotify_stuff(current_song)
                    create_cape(song_name, author_name)
                    cape.update("cape.png")
        time.sleep(1)


def red_fisher():
    # color.put("ff1d1d")
    halo.update("ff1d1d")
    dragon.update("5b5bb9fa-da66-4dff-b53f-c598f0a4c173,1")
    wings.update("ff1d1d,ff1d1d")
    fisher.update("b14685dd-b384-4851-b88a-698c67bc931a")
    hand.update("ff1d1d,1")
    eyes.update("ff1d1d")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def white_fisher():
    # color.put("fdfdfd")
    halo.update("fdfdfd")
    dragon.update("aa26b30f-7761-4f54-ba34-93803f515b97,1")
    wings.update("fdfdfd,fdfdfd")
    fisher.update("edd9718c-5c10-41fa-9af7-03f19ba10799")
    hand.update("fdfdfd,1")
    eyes.update("fdfdfd")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def light_blue_fisher():
    # color.put("00c9ff")
    halo.update("00c9ff")
    dragon.update("24677cb1-7de2-4114-bd4b-fc7174c8cdfa,1")
    wings.update("00c9ff,00c9ff")
    fisher.update("d3b16b9d-954c-4e09-81ef-9e17eebfbca3")
    hand.update("00c9ff,1")
    eyes.update("00c9ff")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def red_horns():
    # color.put("ff1d1d")
    halo.update("ff1d1d")
    horns.update("ff1d1d")
    dragon.update("5b5bb9fa-da66-4dff-b53f-c598f0a4c173,1")
    wings.update("ff1d1d,ff1d1d")
    hand.update("ff1d1d,1")
    eyes.update("ff1d1d")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def white_horns():
    # color.put("fdfdfd")
    halo.update("fdfdfd")
    horns.update("fdfdfd")
    dragon.update("aa26b30f-7761-4f54-ba34-93803f515b97,1")
    wings.update("fdfdfd,fdfdfd")
    hand.update("fdfdfd,1")
    eyes.update("fdfdfd")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def light_blue_horns():
    # color.put("00c9ff")
    halo.update("00c9ff")
    horns.update("00c9ff")
    dragon.update("24677cb1-7de2-4114-bd4b-fc7174c8cdfa,1")
    wings.update("00c9ff,00c9ff")
    hand.update("00c9ff,1")
    eyes.update("00c9ff")
    # cape_border(color)
    cape.update("cape.png")
    time.sleep(interval)


def reset_cosmetics():
    halo.update_visibility(1)
    cape.update_visibility(1)
    fisher.update_visibility(1)
    hand.update_visibility(1)
    eyes.update_visibility(1)
    wings.update_visibility(1)
    dragon.update_visibility(1)
    horns.update_visibility(0)


def cosmetics():
    print("Cosmetics Thread Started")
    reset_cosmetics()
    while True:
        red_fisher()
        white_fisher()
        light_blue_fisher()
        fisher.update_visibility(0)
        horns.update_visibility(1)
        red_horns()
        white_horns()
        light_blue_horns()
        fisher.update_visibility(1)
        horns.update_visibility(0)


cosmeticsThread = Thread(target=cosmetics)
spotifyThread = Thread(target=spotify_cloak)
cosmeticsThread.start()
spotifyThread.start()
cosmeticsThread.join()
spotifyThread.join()
