from config import genius

song_title = 'Ebube'
artist_name = 'Frank Edwards'


def lyrics(title: str, name: str):
    try:
        song = genius.search_song(title, name)
        return song.lyrics
    except BaseException as e:
        return f'{e} No Song available or check your internet connection'
