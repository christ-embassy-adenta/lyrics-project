import lyricsgenius
import spotipy
from decouple import config

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(
    client_id=config('CLIENT_ID'), client_secret=config('CLIENT_SECRET')))

genius = lyricsgenius.Genius(config('GENIUS_ACCESS_TOKEN'))
