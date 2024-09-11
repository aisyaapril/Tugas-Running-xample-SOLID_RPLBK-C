from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def playAudio(self):
        pass

    def playVideo(self):
        pass

class dvdPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di DVD player")

    def playVideo(self):
        print("Memutar video di DVD player")

class winampPlayer(MediaPlayer):
    def playAudio(self):
        print("Memutar audio di Winamp player")

    def playVideo(self):
        raise Exception("Winamp player tidak mendukung pemutaran video")

def play_media(player: MediaPlayer):
    player.playAudio()
    player.playVideo()

dvd = dvdPlayer()
play_media(dvd)

winamp = winampPlayer()
play_media(winamp)
