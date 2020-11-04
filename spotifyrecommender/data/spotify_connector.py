from spotipy.oauth2 import SpotifyClientCredentials
from data.file_loader import get_file
import spotipy

credential_file = "credentials.json"

def get_spotify_client_manager():
    credentials = get_file(credential_file)
    
    client_id = credentials['client_id']
    client_secret = credentials['client_secret']

    client_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    return spotipy.Spotify(client_credentials_manager=client_manager)

