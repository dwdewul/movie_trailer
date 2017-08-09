import webbrowser


class Movie():
    """ A class that initializes a Movie Object
        Movies must provide a title, poster image url,
        and a Youtube trailer url
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
