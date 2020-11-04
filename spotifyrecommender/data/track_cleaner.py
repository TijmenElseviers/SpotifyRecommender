from data.file_loader import get_file
from data.spotify_connector import get_spotify_client_manager
import numpy as np
import pandas as pd

playlists_file = "spotify_playlists.json"
sp = get_spotify_client_manager()

def get_tracks(like):
    playlists = get_file(playlists_file)
    playlist_id = ""

    for playlist in playlists:
        uri = playlist['uri']

        if(playlist['like'] == like):
            playlist_id = uri.split(':')[2]

    return sp.user_playlist("", playlist_id, 'tracks')

def clean_tracks(like):
    playlist_tracks_data = get_tracks(like)['tracks']
    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []

    for track in playlist_tracks_data['items']:
        playlist_tracks_id.append(track['track']['id'])
        playlist_tracks_titles.append(track['track']['name'])
        artist_list = []
        for artist in track['track']['artists']:
            artist_list.append(artist['name'])
        playlist_tracks_artists.append(artist_list)
        playlist_tracks_first_artists.append(artist_list[0])

    features = sp.audio_features(playlist_tracks_id)
    return pd.DataFrame(data=features, columns=features[0].keys())

def clean_console():
    print("\nNo cleaning data to CSV has been implemented yet!")