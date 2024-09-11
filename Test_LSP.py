from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def playAudio(self):
        pass

    @abstractmethod
    def playVideo(self):
        pass

class dvdPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di DVD Player.")

    def playVideo(self):
        print("Memutar video di DVD Player.")

class winampPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di Winamp Player.")

    def playVideo(self):
        raise NotImplementedError("Winamp Player tidak mendukung pemutaran video.")

def play_media(player: MediaPlayer):
    player.playAudio()
    try:
        player.playVideo()
    except NotImplementedError as e:
        print(e)

dvd = dvdPlayer()
play_media(dvd)

winamp = winampPlayer()
play_media(winamp)
