import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time


scope = "user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id="489f6f789db1475fa1cd7703a2be2e11",
                                               client_secret="4fef0ef1a6ce44fea30aa0eebfcd02a1",
                                               redirect_uri="http://localhost:8350/callback/"))


print("logged in")
sp.pause_playback()
print("paused")
time.sleep(2)
sp.start_playback()
print("playing")
time.sleep(2)
volume_change = input("Enter the new percentage of playback you would like: ")
sp.volume(int(volume_change))
print("changed volume to " + volume_change + "%")
time.sleep(2)
sp.volume(int(10))
print("changed volume to 10%")
time.sleep(2)
sp.previous_track()
print("played previous track")
time.sleep(2)
sp.next_track()
print("played next_track")
time.sleep(2)
sp.shuffle(True)
print("playlist shuffled")
song_name = input("Enter the name of the song you want to play: ")
results = sp.search(q=song_name, type='track')
track_uri = results['tracks']['items'][0]['uri']
sp.start_playback(uris=[track_uri])
new_volume = input("Enter the new volume of playback for song above: ")
sp.volume(int(new_volume))
print("playing " + song_name + " at " + new_volume + "%")