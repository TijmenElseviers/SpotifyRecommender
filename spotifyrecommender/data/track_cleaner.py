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

    results = sp.user_playlist_tracks("", playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks


def clean_tracks(like):
    playlist_tracks_data = get_tracks(like)
    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []

    for track in playlist_tracks_data:
        playlist_tracks_id.append(track['track']['id'])
        playlist_tracks_titles.append(track['track']['name'])
        artist_list = []
        for artist in track['track']['artists']:
            artist_list.append(artist['name'])
        playlist_tracks_artists.append(artist_list)
        playlist_tracks_first_artists.append(artist_list[0])


    chunks = [playlist_tracks_id[x:x+100] for x in range (0, len(playlist_tracks_id), 100)]

    features = []
    for chunk in chunks:
            features.extend(sp.audio_features(chunk))

    features_df = pd.DataFrame(data=features, columns=features[0].keys())

    features_df['title'] = playlist_tracks_titles
    features_df['first_artist'] = playlist_tracks_first_artists
    features_df['all_artists'] = playlist_tracks_artists
    features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                            'danceability', 'energy', 'key', 'loudness',
                            'mode', 'acousticness', 'instrumentalness',
                            'liveness', 'valence', 'tempo',
                            'duration_ms', 'time_signature']]

    return features_df

def get_audio_analysis(dataframe):
    num_bars = []
    num_sections = []
    num_segments = []

    for i in range(0, len(dataframe['id'])):
        analysis = sp.audio_analysis(dataframe.iloc[i]['id'])
        num_bars.append(len(analysis['bars']))
        num_sections.append(len(analysis['sections']))
        num_segments.append(len(analysis['segments']))

    dataframe['num_bars'] = num_bars
    dataframe['num_sections'] = num_sections
    dataframe['num_segments'] = num_segments

    return dataframe

def clean_console():
    print("\nNo cleaning data to CSV has been implemented yet!")