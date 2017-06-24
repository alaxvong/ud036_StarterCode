class Media():

    '''
    This class contains information necessary for all media
    '''

    media_list = []  # Array container for future populated instances

    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.media_list.append(self)  # Adds instance to media_list


class Movie(Media):
    # Passing Media as an arguement inherits all of Media's attributes

    '''
    This class provides a way to store movie related information
    '''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Media.__init__(self, title, poster_image_url)
        # Inherited variables still need to be initialized
        self.trailer_youtube_url = trailer_youtube_url
