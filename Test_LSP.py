from abc import ABC, abstractmethod

# Superclass MediaPlayer
class MediaPlayer(ABC):
    @abstractmethod
    def playAudio(self):
        pass

    @abstractmethod
    def playVideo(self):
        pass

# Subclass dvdPlayer
class dvdPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di DVD Player.")

    def playVideo(self):
        print("Memutar video di DVD Player.")

# Subclass winampPlayer
class winampPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di Winamp Player.")

    # Winamp hanya memutar audio, tidak memiliki kemampuan untuk memutar video
    def playVideo(self):
        raise NotImplementedError("Winamp Player tidak mendukung pemutaran video.")

# Fungsi yang menggunakan prinsip Liskov Substitution
def play_media(player: MediaPlayer):
    player.playAudio()
    try:
        player.playVideo()
    except NotImplementedError as e:
        print(e)

# Menggunakan DVD Player
dvd = dvdPlayer()
play_media(dvd)

# Menggunakan Winamp Player
winamp = winampPlayer()
play_media(winamp)
