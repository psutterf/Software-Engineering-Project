import pygame
import random

audio_instance = None

class AudioManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2)

        # music files for gameplay runtime
        self.music_tracks = [
            "sound/Track01.mp3", "sound/Track02.mp3", "sound/Track03.mp3",
            "sound/Track04.mp3", "sound/Track05.mp3", "sound/Track06.mp3",
            "sound/Track07.mp3", "sound/Track08.mp3"]
        self.last_track = None
        pygame.mixer.music.set_volume(0.4)

        # audio files for player sound effects
        self.sounds = {
            "hit" : pygame.mixer.Sound("sound/hit.wav"),
            "get_hit" : pygame.mixer.Sound("sound/gethit.wav"),
            "hit_own" : pygame.mixer.Sound("sound/hitown.wav"),
            "miss" : pygame.mixer.Sound("sound/miss.wav"),
            "reset" : pygame.mixer.Sound("sound/reset.wav") }
        
        for s in self.sounds.values():
            s.set_volume(0.8)

        # event for when the music ends
        self.MUSIC_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.MUSIC_END)

    # randomly selects a music track to use for background
    def play_random_music(self):
        track = random.choice(self.music_tracks)
        while track == self.last_track:
            track = random.choice(self.music_tracks)

        self.last_track = track
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()

    # plays another random track in the event that the previous one ends
    def handle_event(self, event):
        if event.type == self.MUSIC_END:
            self.play_random_music()

    # function for playing sound effects
    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

# initializer for audio use in other files
def get_audio():
    global audio_instance
    if audio_instance is None:
        audio_instance = AudioManager()
    return audio_instance

