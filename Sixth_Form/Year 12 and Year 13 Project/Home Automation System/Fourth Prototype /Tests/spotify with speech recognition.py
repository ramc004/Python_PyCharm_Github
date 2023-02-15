import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
scope = "user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id="489f6f789db1475fa1cd7703a2be2e11",
                                               client_secret="4fef0ef1a6ce44fea30aa0eebfcd02a1",
                                               redirect_uri="http://localhost:8350/callback/"))


def do_spotify_command():
    r_spotify = sr.Recognizer()
    with sr.Microphone() as source_spotify:
        r_spotify.adjust_for_ambient_noise(source_spotify, duration=0.2)
        print("What would you like to do with spotify")
        audio_spotify = r_spotify.listen(source_spotify)
        speech_spotify = r_spotify.recognize_google(audio_spotify)
        if "change volume" in speech_spotify:
            r_volume = sr.Recognizer()
            # variable used to recognise speech
            with sr.Microphone() as source_volume:
                r_volume.adjust_for_ambient_noise(source_volume, duration=0.2)
                print("What would you like the new percentage of playback to be?")
                volume_change = r_volume.listen(source_volume)
                speech_volume = r_volume.recognize_google(volume_change)
                sp.volume(int(speech_volume))
                print("Your volume has been changed to " + speech_volume + "%, if this is the wron"
                                                                           "g volume please retry")
        elif "play" in speech_spotify:
            sp.start_playback()
        elif "pause" in speech_spotify:
            # doesn't work because can hear music in background
            # maybe there's a way to ignore speakers??
            # and only receive input from microphone
            sp.pause_playback()
        elif "song" in speech_spotify:
            r_song = sr.Recognizer()
            with sr.Microphone() as song_user:
                r_song.adjust_for_ambient_noise(song_user, duration=0.2)
                print("Which song would you like to play?")
                song_audio = r_spotify.listen(song_user)
                song_user = r_spotify.recognize_google(song_audio)
                print("You said: " + song_user + ", " + song_user + " is playing, if this"
                                                                    " wasn't the song you wanted to play, please retry")
                results = sp.search(q=song_user, type='track')
                track_uri = results['tracks']['items'][0]['uri']
                sp.start_playback(uris=[track_uri])
        elif "shuffle" in speech_spotify:
            sp.shuffle(True)
        elif "skip" or "next" in speech_spotify:
            sp.next_track()
        elif "previous" or "go back" in speech_spotify:
            sp.previous_track()
        else:
            print("retry")


r_for_spotify = sr.Recognizer()
# variable used to recognise speech

with sr.Microphone() as source_for_spotify:
    r_for_spotify.adjust_for_ambient_noise(source_for_spotify, duration=0.2)
    print("Speak now")
    audio_for_spotify = r_for_spotify.listen(source_for_spotify)

    speech_for_spotify = r_for_spotify.recognize_google(audio_for_spotify)

    print("You said: " + speech_for_spotify)
    if "Spotify" in speech_for_spotify:
        do_spotify_command()
