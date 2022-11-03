"""
This is the media player class. It is a wrapper around the vlc.MediaPlayer class.
"""
from typing import Callable

import pafy  # type:ignore
import vlc  # type:ignore


class MediaPlayer:
    """
    MediaPlayer class
    """

    def __init__(self):

        self.current_media: dict = {
            "album": None,
            "artists": None,
            "duration": None,
            "thumbnail": None,
            "title": None,
            "videoId": None,
            "year": None
        }
        self.state: str = "Idle"
        self.queue: list = []
        self.player = vlc.MediaPlayer()

    def load_media(self, media: dict, callback: Callable = print) -> None:
        """
        Loads selected media to player
        :param callback: callback function for when the media is loaded
        :param media: dictionary of media information
        :return: None
        """
        media_file = pafy.new(media["videoId"]).getbestaudio().url
        self.player.set_mrl(media_file)
        self.current_media = media
        self.state = "Loaded"
        callback("Loaded")

    def pause(self, callback: Callable = print) -> None:
        """
        Plays paused media and pauses playing media
        :param callback: function to return state of player
        :return: None
        """
        state = self.player.get_state()
        if state == vlc.State.Paused:
            self.state = "Playing"
        elif state == vlc.State.Playing:
            self.state = "Paused"
        self.player.pause()

        callback(self.state)

    def play(self, callback: Callable = print) -> None:
        """
        Plays the media
        :return: None
        """
        self.player.play()
        self.state = "Playing"
        callback(self.state)

    def stop(self, callback: Callable = print) -> None:
        """
        Stops the media
        :return: None
        """
        self.player.stop()
        self.current_media = {
            "album": None,
            "artists": None,
            "duration": None,
            "thumbnail": None,
            "title": None,
            "videoId": None,
            "year": None
        }
        self.state = "Idle"
        callback("Stopped")

    def seek(self, position: float) -> None:
        """
        Set position of media player.
        :param position: float in range [0, 1]
        :return: None
        """
        self.player.set_position(position)

    def position(self) -> float:
        """
        Get position of media player.
        :return: float in range [0, 1]
        """
        return self.player.get_position()

    def get_state(self) -> str:
        """
        Checks current state of media
        :return: Current state of media player
        states include:
        - Idle
        - Loaded
        - Playing
        - Paused
        """
        return self.state

    def queue_media(self, media: dict):
        """
        Adds media to queue
        :param media: dictionary of media information
        :return: None
        """
        self.queue.append(media)

    def get_queue(self) -> list:
        """
        :return: current queue
        """
        return self.queue

    def next(self) -> None:
        """
        Play the next media in queue
        :return: None
        """
        if len(self.queue) > 0:
            media: dict = self.queue.pop(0)
            self.load_media(media)

    def autoplay(self) -> None:
        """
        Checks if current media has ended and plays the next song.
        :return:
        """
        while True:
            if self.get_state() != "Idle":
                state = self.player.get_state()
                if state == vlc.State.Ended:
                    self.next()
