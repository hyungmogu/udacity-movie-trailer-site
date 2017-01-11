"""
What is media.py for?

It houses all data-structures used by the program. The data-structures must be relevant to media.

"""
class Video():

    
    def __init__(self,title,storyline,poster_image_url,trailer_youtube_url,duration):
        self.title               = title
        self.storyline           = storyline
        self.poster_image_url    = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration            = duration

class Movie(Video):
    """
    Movie(Video)
        
    This data-structure stores information about movies. It is a child of Video Class.

    @allowed_attributes:
        - title *
        - storyline *
        - poster_image *
        - youtube_trailer *
        - duration *

    * - inherited attributes
    ** - non-inheritied attributes
    """

    def __init__(self,title,storyline,poster_image,youtube_trailer,duration):
        Video.__init__(self,title,storyline,poster_image,youtube_trailer,duration)


class TvShow(Video):
    """
    TvShow(Video)
        
    This data-structure stores information about TvShows. It is a child of Video Class.

    @allowed_attributes:    
        - title *
        - storyline *
        - season **
        - episode **
        - tv_station **
        - poster_image *
        - youtube_trailer *
        - duration *
   
    * - inherited attributes
    ** - non-inheritied attributes

    """
    def __init__(self,title,storyline,season,episode,tv_station,poster_image,youtube_trailer,duration):
        Video.__init__(self,title,storyline,poster_image,youtube_trailer,duration)
        self.sesason = season
        self.episode = episode
        self.tv_station = tv_station





