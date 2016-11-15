# import webbrowser
# if __name__ == "__main__":
#     print("Notice: Running main.py in the __main__")

# else:
#     print("Notice: Successfully Imported " + __name__ + ".py")

class Video():

    def __init__(self,title,storyline,poster_image_url,trailer_youtube_url,duration):
        self.title               = title
        self.storyline           = storyline
        self.poster_image_url    = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration            = duration

class Movie(Video):
    """
    This class provides a way to store information about movies

    - title *
    - storyline *
    - poster_image *
    - youtube_trailer *
    - duration *

    """

    def __init__(self,title,storyline,poster_image,youtube_trailer,duration):
        Video.__init__(self,title,storyline,poster_image,youtube_trailer,duration)


class TvShow(Video):
    """
        - title *
        - storyline *
        - season
        - episode
        - tv_station
        - poster_image *
        - youtube_trailer *
        - duration *
    """
    def __init__(self,title,storyline,season,episode,tv_station,poster_image,youtube_trailer,duration):
        Video.__init__(self,title,storyline,poster_image,youtube_trailer,duration)
        self.sesason = season
        self.episode = episode
        self.tv_station = tv_station





