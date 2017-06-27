# Class to support Movie Trailer Website.
import webbrowser


class Movie():
    """
    This class includes methods to build the Movie Trailer Website.
    @method __init__()	is the constructor that initializes variables.
    @method show_trailer()	Shows a YouTube movie trailer via the Wen Browser.
    """
    def __init__(self, m_title, m_storyline, m_poster, m_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = m_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
