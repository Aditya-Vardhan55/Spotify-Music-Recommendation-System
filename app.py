import pickle
import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "5732c161f87946eaa8f222b18a4a7103"
CLIENT_SECRET = "ec5a286e759844c7b46b6fb4716d4ac9"

# Initialize the Spotify Client
client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret= CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist{artist_name}"
    results = sp.search(q= search_query, type="track")
    
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return ""