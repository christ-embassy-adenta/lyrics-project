import lyricsgenius
from decouple import config

genius = lyricsgenius.Genius(config('GENIUS_ACCESS_TOKEN'))
