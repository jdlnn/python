class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the TV on if status is not False.
        Then turn the TV off if status is not True.
        """
        self.__status = not self.__status
        if self.__status:
            print('TV is on')
        else:
            print('TV is off')

    def mute(self) -> None:
        """
        Mute and Unmute the TV.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
                print('TV is muted')
            else:
                self.__muted = False
                self.__volume = Television.MIN_VOLUME
                print('TV is unmuted')



    def channel_up(self) -> None:
        """"
        Increases the channel by one. 
        If channel is max, it goes back to min channel. 
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel by one.
        If channel is min, it goes back to max channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increased the volume by one when the status is on and not muted,
        and up to the max volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MAX_VOLUME
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one when the status is on and not muted,
        and down to min volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MAX_VOLUME
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self) -> str:
        """
        Returns the current TV's power, channel, and volume.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

