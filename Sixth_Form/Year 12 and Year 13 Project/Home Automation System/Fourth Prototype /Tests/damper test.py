import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
scope = "user-modify-playback-state, user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id="489f6f789db1475fa1cd7703a2be2e11",
                                               client_secret="4fef0ef1a6ce44fea30aa0eebfcd02a1",
                                               redirect_uri="http://localhost:8350/callback/"))


song = sp.current_playback()
if song:
    currVolume = song["device"]["volume_percent"]
    print(currVolume)

    sp.volume(int(10))
    time.sleep(3)
    sp.volume(int(currVolume))

